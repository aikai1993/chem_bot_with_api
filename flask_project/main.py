from flask import Flask, render_template
from markupsafe import escape
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
  host="localhost",
  user=db_user,
  password=db_password,
  database='chem_bot'
)

cursor = mydb.cursor()

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('hello.html')

@app.route('/chem/')
def chem():
    cursor.execute('SELECT * FROM users;')
    print(cursor.fetchall())
    return render_template('chem.html')

@app.route('/user/<username>')
def hello_user(username):
    return render_template('user.html', name=username)

@app.route('/calc/<int:first_num>/<int:second_num>')
def calc(first_num: int, second_num: int):
    return f'{first_num + second_num}'
