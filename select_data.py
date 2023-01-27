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

def select_all(conn, table):
    
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    rows = cur.fetchall()

    return rows

def select_where(conn, table, **query):
    cur = conn.cursor()
    qs = []
    values = ()
    for k, v in query.items():
        qs.append(f"{k}=?")
        values += (v,)
    q = " AND ".join(qs)
    cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
    rows = cur.fetchall()

    return rows

if __name__ == "__main__":
   
    conn = create_connection(db_file="database.db")

    all_authors = select_all(conn, table = "author")
    all_books = select_all(conn, table = "book")

    print(all_authors)
    print(all_books)

    not_read = select_where(conn, table = "book", read = "Not Yet")
    print(not_read)
