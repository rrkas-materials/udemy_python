import psycopg2

connect_string = 'dbname=postgres user=rohnak password=rohnak host=localhost port=5432'


def create_table():
    conn = psycopg2.connect(connect_string)
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


def insert(item, qty, price):
    conn = psycopg2.connect(connect_string)
    cur = conn.cursor()
    cur.execute('INSERT INTO store (item, quantity, price) VALUES(%s, %s, %s)', (item, qty, price))  # better tha later option
    # OR
    # cur.execute("INSERT INTO store (item, quantity, price) VALUES('%s', %s, %s)" % (item, qty, price))
    # note: postgres cannot accept "value", it only accepts 'value'
    conn.commit()
    conn.close()


def update_quantity(item, qty, price):
    conn = psycopg2.connect(connect_string)
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity=%s, price=%s WHERE item=%s', (qty, price, item))
    conn.commit()
    conn.close()


def delete(item):
    conn = psycopg2.connect(connect_string)
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item=%s', (item,))
    conn.commit()
    conn.close()


def view():
    conn = psycopg2.connect(connect_string)
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    for r in rows:
        print("{:10s}\t|\t{:3d}\t|\t{:7.2f}".format(r[0], r[1], r[2]))
    print('-------------------------------')


if __name__ == "__main__":
    create_table()
    insert('Rubber', 1, 25)
    insert('Steel', 1, 20)
    insert('Wood', 1, 15)
    insert('Plastic', 2, 12)
    view()
    update_quantity('Wood', 5, 15)
    view()
    delete('Steel')
    view()
