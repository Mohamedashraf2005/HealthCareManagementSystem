# idlistdoctor = [
#     1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
#     11, 12, 13, 14, 15, 16, 
# ]


import sqlite3
import os

db_path = os.path.join(os.path.dirname(__file__), '..', 'database', 'HCMSclinic.db')

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

xx = "SELECT id FROM doctor"
cursor.execute(xx)

idlistdoctor = [row[0] for row in cursor.fetchall()]

print("Doctor IDs:", idlistdoctor )

cursor.close()
connection.close()