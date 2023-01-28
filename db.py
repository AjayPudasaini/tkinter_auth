import sqlite3

with sqlite3.connect("mydatabase.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL, email text NOT NULL, full_name text NOT NULL); """)
