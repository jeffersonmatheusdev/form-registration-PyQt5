import os
import sqlite3

class CRUD():
    def __init__(self):
        self.data = sqlite3.connect(r'{}\\DB\\users.db'.format(os.getcwd()))
        self.cursor = self.data.cursor()
        self.createTabe()

    def createTabe(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTERGER,
                email TEXT,
                password TEXT
            )""")
        self.data.commit()

    def insert(self, name, age, email, password):
        self.cursor.execute("""
            INSERT INTO users (name, age, email, password)
            VALUES (?, ?, ?, ?)""", (name, age, email, password))
        self.data.commit()

    def select(self, email):
        self.cursor.execute("""
            SELECT * FROM users
            WHERE email = ?""", (email,))
        return self.cursor.fetchall()
    
    def update(self, name, age, email, password):
        self.cursor.execute("""
            UPDATE users
            SET name = ?, age = ?, email = ?, password = ?
            WHERE email = ?""", (name, age, email, password, email))
        self.data.commit()

    
    def delete(self, email):
        self.cursor.execute("""
            DELETE FROM users
            WHERE email = ?""", (email,))
        self.data.commit()