import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")

mydb = mysql.connector.connect(
  host="chem_db",
  user=db_user,
  password=db_password,
  database='chem_bot'
)

cursor = mydb.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users (
    tg_id INT PRIMARY KEY,
    brt VARCHAR(50)           
)''')

# cursor.execute ("DROP TABLE users_history")

cursor.execute('''CREATE TABLE IF NOT EXISTS users_history (
    id INT PRIMARY KEY AUTO_INCREMENT,
    tg_id INT NOT NULL,
    brt VARCHAR(50),
    smiles VARCHAR(512),
    date_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP         
)''')

# cursor.execute ("DROP TABLE users_hash")

cursor.execute('''CREATE TABLE IF NOT EXISTS users_hash (
    tg_id INT NOT NULL PRIMARY KEY,
    hash VARCHAR(20)        
)''')



mydb.commit()