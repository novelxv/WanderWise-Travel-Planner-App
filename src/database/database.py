import sqlite3
import os

def connect_db():
    cwd = os.path.dirname(__file__)
    path = os.path.join(cwd, 'wanderwise.db')

    if not os.path.exists(path):
        print("Creating database!")
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        with open(os.path.join(cwd, 'schema.sql')) as f:
            cursor.executescript(f.read()) 
        conn.commit()
        conn.close()
        return conn,cursor
    else:
        conn = sqlite3.connect(path)
        cursor = conn.cursor()
        return conn,cursor
    
def clear_db():
    tables = ["t_itinerary", "t_artikel", "t_destinasi"]
    for table in tables:
        cursor.execute(f"DELETE FROM {table}")
        cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}'")
    commit()

def commit():
    conn.commit()

def __del__():
    conn.close()

conn, cursor = connect_db()