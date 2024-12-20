import os
import sqlite3

db_path = os.path.join(os.path.dirname(__file__), 'HCMSclinic.db')

#Ashraf-check if Name is valid in table database
def checkname(name):
    for i in name: 
        if not (i.isalpha() or i.isspace()):
            return False
    return True 
#eman mohamed creat 2 fanctions : 1=>check for username
#                                 2=>check for password
def create_database():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS patient (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def add_patient(username, password):
    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patient (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
    except sqlite3.IntegrityError:
        print("username already exist")
    finally:
        conn.close()
def check_username(username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False
def check_password(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patient WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False
if __name__ == "__main__":
    create_database()
    username = input("enter username ")
    if check_username(username):
        print("username exist")
    else:
        print("username doesnot exist")
    password = input(" enter password" )
    if check_password(username, password):
        print("you are register successfuly")
    else:
        print("password wrong")