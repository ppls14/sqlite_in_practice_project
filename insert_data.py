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

def add_author(conn, author):
    sql = """
    INSERT INTO author (name, surname, born, nationality, books_written)
    VALUES (?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, author)
    conn.commit()

    return cur.lastrowid

def add_book(conn, book):
    sql = """
    INSERT INTO book (title, type, publication, read, author_id)
    VALUES (?,?,?,?,?)
    """
    cur = conn.cursor()
    cur.execute(sql, book)
    conn.commit()

    return cur.lastrowid

if __name__ == "__main__":

    conn = create_connection("database.db")

    chuck_palahniuk = ("Chuck", "Palahniuk", "21-02-1962", "American", 25 )
    walter_isaacson = ("Walter", "Isaacson", "20-05-1952", "American", 8)
    stanislaw_lem = ("Stanisław", "Lem", "12-09-1921", "Polish", 38)

    fightclub = ("Fight Club", "Novel", "August 17th, 1996", "Done", add_author(conn, author = chuck_palahniuk))
    add_book(conn, book=fightclub)
    leonardo = ("Leonardo Da Vinci", "Biography", "April 14th, 2012", "Not Yet", add_author(conn, author = walter_isaacson))
    add_book(conn, book=leonardo)
    solaris = ("Solaris", "Novel", "March 30th, 1961", "Not Yet", add_author(conn, author=stanislaw_lem))
    add_book(conn, book=solaris)

    conn.commit()