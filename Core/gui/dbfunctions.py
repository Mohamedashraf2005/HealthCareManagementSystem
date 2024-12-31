import os
import sqlite3
from idoctorlist import idlistdoctor
from idpatientlist import idlistpatient 

#if you want connect with database write inside connect (db_path) مهم مهم مهم مهم مهم 
db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

#Ashraf-check if Name is valid in table database
def checkname(name): #Signup class
    for i in name: 
        if not (i.isalpha() or i.isspace()):
            return False
    return True 

def input_age(age):  #Admin ,Signup class
    try:
        age = int(age)  
        if 0 <= age <= 120: 
              return age
        else:
            print("Invalid input: Age must be between 0 and 120.")
            return None
    except ValueError:  
        print("Invalid input: Must be a numeric value.")
        return None

def check_gender (gender):
    if gender.lower() == "male" or "female" :
        return gender
    else :
        print("enter valid gender Male or Female")
        return None

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

#####################
def check_usernameD(username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctor WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False
def check_passwordD(username, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctor WHERE username = ? AND password = ?", (username, password))
    result = cursor.fetchone()
    conn.close()
    if result:
        return True
    else:
        return False


def usernametodahboarf(usernameget):
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM patient WHERE username = ?", (usernameget,))
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        result = None
    finally:
        conn.close()
    return result[2]

def returnidlolo(usernamegetter):
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM patient WHERE username = ?", (usernamegetter,))
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        result = None
    finally:
        conn.close()
    return result[0]

def usernametodahboardoctor(usernamegetter):
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM doctor WHERE username = ?", (usernamegetter,))
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        result = None
    finally:
        conn.close()
    return result[2]

def OTPVerify(ourOTP):
    # Convert the OTP to integer
    
    checkotpid = int(ourOTP)  # Convert the OTP to an integer    
    # Check if the OTP ID is in the idlistpatient
    if checkotpid in idlistpatient:
        print("VALID OTP")
        return True
    else:
        print("INVALID OTP")
        return False
    
def OTPVerifydoctor(ourOTP2):
    # Convert the OTP to integer
    
    checkotpiddoc = int(ourOTP2)  # Convert the OTP to an integer    
    # Check if the OTP ID is in the idlistpatient
    if checkotpiddoc in idlistdoctor:
        print("VALID OTP")
        return True
    else:
        print("INVALID OTP")
        return False
    
def returnidnono(usernamegetter):
    conn = sqlite3.connect(db_path)  
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM doctor WHERE username = ?", (usernamegetter,))
        result = cursor.fetchone()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        result = None
    finally:
        conn.close()
    return result[0]




