import sqlite3 
from sqlite3 import Error

def create_connection(db_file):
    """Create database connection to a SQLite database and return an object with established connection"""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version {sqlite3.version}")
        return conn 
    except Error as e:
        print(e)

    return conn

if __name__ == "__main__":
    create_connection(r"database.db")