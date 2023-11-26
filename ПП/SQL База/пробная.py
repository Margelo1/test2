import sqlite3

conn = sqlite3.connect('База.db')

cursor = conn.cursor()

cursor.execute('Select * from Pacient')

result = cursor.fetchall()

print(result)

conn.commit()

conn.close()
