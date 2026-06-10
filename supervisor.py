import sqlite3

banco = sqlite3.connect('supervisor.db')

cursor = banco.cursor()

#cursor.execute("CREATE TABLE supervisor (Nome text, Codigo integer)")

cursor.execute("INSERT INTO supervisor VALUES ('Kaio', 2530)")

banco.commit()
"""cursor.execute("SELECT * FROM supervisor")
print(cursor.fetchall())"""