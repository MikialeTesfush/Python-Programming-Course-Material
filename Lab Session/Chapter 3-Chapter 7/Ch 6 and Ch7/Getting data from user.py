import sqlite3
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
age = int(input("Enter your age: "))
with sqlite3.connect("database.db") as connection:
    cursor = connection.cursor()
    cursor.execute("""CREATE TABLE People(FirstName TEXT,LastName TEXT,Age INT)""")
    cursor.execute(f"INSERT INTO People Values('{first_name}', '{last_name}', {age});")
    cursor.execute("SELECT * FROM People;")
    print(cursor.fetchone())
