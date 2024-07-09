from flask import Flask, render_template
from markupsafe import escape
import mysql.connector
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

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
    return render_template('chem.html', brt_mol=brt_mol)

@app.route('/user/<username>')
def hello_user(username):
    return render_template('user.html', name=username)

@app.route('/calc/<int:first_num>/<int:second_num>')
def calc(first_num: int, second_num: int):
    return f'{first_num + second_num}'
