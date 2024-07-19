from flask import Flask, render_template
from markupsafe import escape
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime
import requests
from rdkit import Chem
from rdkit.Chem import Draw

load_dotenv()

images = os.path.join('static', 'images')

db_user = os.getenv('DB_USER')
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
  host="chem_db",
  user=db_user,
  password=db_password,
  database='chem_bot'
)

cursor = mydb.cursor()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route('/chem/<hash_id>')
def chem(hash_id):
    mydb.reconnect()
    cursor.execute('SELECT * FROM users_hash where hash = %s;', (hash_id,))
    tg_id = cursor.fetchone()[0]
    cursor.execute('SELECT * FROM users_history where tg_id = %s;', (tg_id,))
    all_history = cursor.fetchall()
    brt_mol = [(x[2] if x[2] else "", x[3] if x[3] else "", x[5].strftime('%d.%m.%Y %H:%M:%S'), x[4]) for x in all_history]
    [
        ('H20', "", '05.07.2024 17:04:41', 1),
        ('sdfsdfsdf', "", '05.07.2024 17:04:54', 0)
    ]
    return render_template('chem.html', brt_mol=brt_mol)



@app.route('/brt/<formula>')
def brt(formula):
    brt_from_api = requests.get(f'http://chem_api/calc/{formula}').json()
    brt_list = sorted(list(brt_from_api['elements'].items()), key=lambda x: (x[0] not in 'CH', x[0]))
    return render_template('brt.html', formula=formula, total_mass=brt_from_api['total_mass'], brt_list=brt_list)





# def draw_mol(message):
#     try:
#         m = Chem.MolFromSmiles(message.text)
#         kanon_m = Chem.MolToSmiles(m)
#         cursor.execute('INSERT INTO users_history(tg_id, smiles, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, kanon_m, 1))
#         mydb.commit()
#         images = os.listdir('images')
        
#         if f'{kanon_m}.png' not in images:
#             img = Draw.MolToImage(m)
#             img.save(f'images/{kanon_m}.png')

#         bot.send_photo(message.from_user.id, photo=open(f'images/{kanon_m}.png', 'rb'))
#     except Exception as error:
#         cursor.execute('INSERT INTO users_history(tg_id, smiles, is_valid) VALUES (%s, %s, %s)', (message.from_user.id, message.text, 0))
#         mydb.commit()
#         print(error)
#         bot.send_message(message.from_user.id, f'Некорректный ввод. Попробуйте снова:')
#         bot.register_next_step_handler(message, draw_mol)



@app.route('/mol/<smiles>')
def mol(smiles):
    try:
        m = Chem.MolFromSmiles(smiles)
        kanon_m = Chem.MolToSmiles(m)
        if f'{kanon_m}.png' not in os.listdir(images):
            img = Draw.MolToImage(m)
            img.save(os.path.join(images, f'{kanon_m}.png'))
        image_path = os.path.join(images, f'{kanon_m}.png')
        return render_template('mol.html', smiles=smiles, image=image_path)
    except Exception as e:
        print(e)
        return str(e)
    