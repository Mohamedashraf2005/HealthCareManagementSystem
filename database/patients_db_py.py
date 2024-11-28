import sqlite3

db=sqlite3.connect("patients.db")
cursordb= db.cursor()

cursordb.execute("SELECT * FROM patients")

results= cursordb.fetchall()
print(results[0])
print(f"Databse has {len(results)} Rows")

db.commit()
db.close()