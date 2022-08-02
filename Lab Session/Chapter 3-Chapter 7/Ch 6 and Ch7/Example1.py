import sqlite3
connection = sqlite3.connect("test_database.db")
cursor = connection.cursor()
cursor.execute("""CREATE TABLE People(FirstName TEXT,LastName TEXT,Age INT);""")
cursor.execute("""INSERT INTO People VALUES('Ron','Obvious',42);""")
connection.commit()
connection.close()