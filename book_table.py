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

def execute_sql(conn, sql):
    """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

if __name__ == "__main__":

    book_sql = """
    -- book table
    CREATE TABLE book (
        id              integer PRIMARY KEY,
        author_id       integer NOT NULL,
        title           text NOT NULL,
        type            text NOT NULL,
        publication     text NOT NULL,
        read            text NOT NULL,
        FOREIGN KEY (author_id) REFERENCES author (id)
    );
    """

    conn = create_connection(db_file = "database.db")
    execute_sql(conn, sql = book_sql)