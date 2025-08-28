import sqlite3

DB_NAME = "todo_app.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_tables():
    with get_connection() as conn:
        cursor = conn.cursor()
        with open("schema.sql", "r", encoding="utf-8") as f:
            cursor.executescript(f.read())
        conn.commit()
