import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to {db_file}, sqlite version {sqlite3.version}")
        return conn 
    except Error as e:
        print(e)

    return conn

def delete_all(conn, table):

    sql = f'DELETE FROM {table}'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    print(f"All {table} table data, deleted.")

def delete_where(conn, table, **kwargs):

    qs = []
    values = tuple()
    for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
    q = " AND ".join(qs)

    sql = f'DELETE FROM {table} WHERE {q}'
    cur = conn.cursor()
    cur.execute(sql, values)
    conn.commit()
    print(f"Table {table} data of id = {id}, deleted")

if __name__ == "__main__":

    conn = create_connection(db_file = "database.db")
    delete_where(conn, table = "author", id = 3)
    delete_all(conn, table = "book")
    
    conn.close()