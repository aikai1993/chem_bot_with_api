import telebot
from telebot import types
from rdkit import Chem
from rdkit.Chem import Draw
import os
from dotenv import load_dotenv
import requests
from db import *
from hashids import Hashids


load_dotenv()

bot_token = os.getenv('TOKEN')
bot = telebot.TeleBot(bot_token)

hashids = Hashids(salt='this is my salt 1', min_length=20)


@bot.message_handler(commands=['start'])
def start(message):
    cursor.execute('Select * from users where tg_id = %s', (message.from_user.id, ))
    if not cursor.fetchall():
        cursor.execute('INSERT INTO users(tg_id) VALUES (%s)', (message.from_user.id, ))
        mydb.commit()

    cursor.execute('Select * from users_hash where tg_id = %s', (message.from_user.id, ))
    if not cursor.fetchall():
        cursor.execute('INSERT INTO users_hash(tg_id, hash) VALUES (%s, %s)', (message.from_user.id, hashids.encode(message.from_user.id)))
        mydb.commit()

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    calc_button = types.KeyboardButton('/calc')
    mol_button = types.KeyboardButton('/mol')
    req_button = types.KeyboardButton('/history')
    keyboard.add(calc_button, mol_button, req_button)

    bot.send_message(message.from_user.id, '\n\n'.join(('Привет! Я Химический Бот!',
    'Если Вы хотите получить изображение молекулы по формуле SMILES, введите /mol',
    'Если Вы хотите посчитать молекулярную массу по брутто-формуле, введите /calc',
    'Если Вы хотите посмотреть историю запросов, введите /history')),
    reply_markup=keyboard)

@bot.message_handler(commands=['mol'])
def mol(message):
    bot.send_message(message.from_user.id, 'Введите молекулу:')
    bot.register_next_step_handler(message, draw_mol)

@bot.message_handler(commands=['calc'])
def calc(message):
    bot.send_message(message.from_user.id, 'Введите брутто-формулу:')
    bot.register_next_step_handler(message, calc_brutto)

@bot.message_handler(commands=['history'])
def history(message):
    cursor.execute('Select hash from users_hash where tg_id = %s', (message.from_user.id, ))
    user_hash = cursor.fetchone()[0]
    text = f'История запросов: http://91.214.242.240:5000/chem/{user_hash}'
    bot.send_message(message.from_user.id, text)

def calc_brutto(message):
    b = message.text
    cursor.execute('UPDATE users SET brt = %s WHERE tg_id = %s', (b, message.from_user.id))
    mydb.commit()
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    mol_mass_button = types.KeyboardButton('Молекулярная масса вещества')
    mol_mass_exact_button = types.KeyboardButton('Моноизотопная молекулярная масса вещества')
    elem_analysis_button = types.KeyboardButton('Данные элементного анализа')
    all_button = types.KeyboardButton('Полный расчет')
    keyboard.add(mol_mass_button, mol_mass_exact_button, elem_analysis_button, all_button)

    bot.send_message(message.from_user.id, 'Выберите из вариантов:', reply_markup=keyboard)

def draw_mol(message):
    try:
        m = Chem.MolFromSmiles(message.text)
        kanon_m = Chem.MolToSmiles(m)
        cursor.execute('INSERT INTO users_history(tg_id, smiles, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, kanon_m, 1))
        mydb.commit()
        images = os.listdir('images')
        
        if f'{kanon_m}.png' not in images:
            img = Draw.MolToImage(m)
            img.save(f'images/{kanon_m}.png')

        bot.send_photo(message.from_user.id, photo=open(f'images/{kanon_m}.png', 'rb'))
    except Exception as error:
        cursor.execute('INSERT INTO users_history(tg_id, smiles, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, message.text, 0))
        mydb.commit()
        print(error)
        bot.send_message(message.from_user.id, f'Некорректный ввод. Попробуйте снова:')
        bot.register_next_step_handler(message, draw_mol)


def print_elements(j):
    elements = ['Элементы:']
    for element, elem_info in j.items():
        elements.append(f'<b>{element}</b>:\n\t\t\tСодержание: {elem_info['percent']}%\n\t\t\tМасса: {elem_info['mass']}')
    return '\n'.join(elements)

def print_total(j):
    total_mass = j['total_mass']
    text = f'Молекулярная масса: {total_mass} Да\n'
    elements = print_elements(j['elements'])
    text = f'{text}\n{elements}'
    return text


def try_request(brt, slug, message):
    try:
        r = requests.get(f'http://chem_api/{slug}/{brt}').json()
        cursor.execute('INSERT INTO users_history(tg_id, brt, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, brt, 1))
        mydb.commit()
        return r
    except Exception as error:
        cursor.execute('INSERT INTO users_history(tg_id, brt, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, brt, 0))
        mydb.commit()
        bot.send_message(message.from_user.id, 'Вы ввели некорректную формулу. Попробуйте снова:')
        bot.register_next_step_handler(message, calc_brutto)    



@bot.message_handler(content_types=['text'])
def text_message(message):
    t = message.text.lower()

    cursor.execute(f'SELECT brt FROM users where tg_id = %s', (message.from_user.id, ))
    last_user_brt = cursor.fetchone()[0]

    if t == 'молекулярная масса вещества':
        answer = try_request(last_user_brt, 'calc', message)['total_mass']
        bot.send_message(message.from_user.id, answer)

    elif t == 'моноизотопная молекулярная масса вещества':
        answer = try_request(last_user_brt, 'calc_exact', message)['total_mass']
        bot.send_message(message.from_user.id, answer)

    elif t == 'данные элементного анализа':
        answer = try_request(last_user_brt, 'elem_analysis', message)
        bot.send_message(message.from_user.id, print_elements(answer), parse_mode='HTML')

    elif t == 'полный расчет':
        answer = try_request(last_user_brt, 'calc', message)
        bot.send_message(message.from_user.id, print_total(answer), parse_mode='HTML')
    else:
        bot.send_message(message.from_user.id, "Извините, я не понимаю :(")


bot.polling(none_stop=True, interval=0)

