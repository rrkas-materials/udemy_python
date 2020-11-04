import psycopg2


def create_table():
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, qty, price):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES (?, ?, ?)', (item, qty, price))
    conn.commit()
    conn.close()


def update_quantity(item, qty, price):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=?, price=? WHERE item=?', (qty, price, item))
    conn.commit()
    conn.close()


def delete(item):
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=?', (item,))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect('lite.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    # create_table()
    # insert('Rubber',1,25)
    # insert('Steel', 1, 25)
    # insert('Wood', 1, 25)
    # insert('Copper', 1, 25)
    # print(view())
    update_quantity('Coffee Cup', 5, 15)
    # print(view())
    # delete('Steel')
    print(view())
