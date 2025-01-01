# idlistpatient = [
#      1,  2,  3,  4,  5,  6,  7,  8,  9, 10,
#     11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
#     21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
#     31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
#     41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
#     51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 
#     61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
# ]


import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

xx = "SELECT id FROM patient"
cursor.execute(xx)

idlistpatient = [row[0] for row in cursor.fetchall()]

print("Patient IDs:", idlistpatient )

cursor.close()
connection.close()