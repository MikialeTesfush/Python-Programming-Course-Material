import sqlite3
connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("SELECT * FROM People;")
print(cursor.fetchone())
