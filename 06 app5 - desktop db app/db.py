import sqlite3


def connect():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
    conn.commit()
    conn.close()


def insert(title, author, year, isbn):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)',(title, author, year, isbn))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM books')
    data = curr.fetchall()
    conn.close()
    return data


def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?',(title, author, year, isbn))
    data = curr.fetchall()
    conn.close()
    return data

def delete(id):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('DELETE FROM books WHERE id=?',(id,))
    conn.commit()
    conn.close()


def update(id,title,author,year,isbn):
    conn = sqlite3.connect('books.db')
    curr = conn.cursor()
    curr.execute('UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?',(title,author,year,isbn,id))
    conn.commit()
    conn.close()

connect()