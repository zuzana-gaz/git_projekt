import sqlite3

connection = sqlite3.connect("mesto_zilina.db")
cursor = connection.cursor()

cursor.execute("SELECT kod FROM zmluvy")
print(cursor.fetchone())
print(cursor.fetchall())

connection.close()
