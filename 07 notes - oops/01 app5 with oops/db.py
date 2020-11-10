import sqlite3

class Database:

    def __init__(self, db):
        #constructor
        self.conn = sqlite3.connect(db)
        self.curr = self.conn.cursor()
        self.curr.execute('CREATE TABLE IF NOT EXISTS books (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)')
        self.conn.commit()

    def __del__(self):
        #destructor
        self.conn.close()

    def insert(self,title, author, year, isbn):
        self.curr.execute('INSERT INTO books VALUES (NULL, ?, ?, ?, ?)',(title, author, year, isbn))
        self.conn.commit()

    def view(self):
        self.curr.execute('SELECT * FROM books')
        data = self.curr.fetchall()
        return data

    def search(self,title='', author='', year='', isbn=''):
        self.curr.execute('SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?',(title, author, year, isbn))
        data = self.curr.fetchall()
        return data

    def delete(self,id):
        self.curr.execute('DELETE FROM books WHERE id=?',(id,))
        self.conn.commit()

    def update(self,id,title,author,year,isbn):
        self.curr.execute('UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?',(title,author,year,isbn,id))
        self.conn.commit()