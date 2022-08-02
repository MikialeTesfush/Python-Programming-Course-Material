import sqlite3
conn=sqlite3.connect("student.db")
print("Database Opened successfully")
conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('admin', 'mikiyo')")
conn.execute("INSERT INTO ADMIN(USERNAME,PASSWORD) VALUES ('mayko', 'miki12')")
conn.commit()
print("Records inserted successfully")
conn.close()