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

def update(conn, table, id, **kwargs):

    parameters = (f"{k}=?" for k in kwargs)
    parameters = "' ".join(parameters)
    values = tuple(v for v in kwargs.values())
    values += (id, )

    sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''
    
    try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print(f"Update in table: {table}, executed.")

    except sqlite3.OperationalError as e:
       print(e)

if __name__ == "__main__":
   
   conn = create_connection(db_file = "database.db")
   update(conn, "book", 2, read = "Done")
   update(conn, "book", 3, read = "Done")
   conn.close()