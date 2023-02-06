import sqlite3 as sl


with sl.connect('my-test.db') as db:
    cursor = db.cursor()
    query = """ INSERT INTO expenses (id, name) VALUES(1, 'коммуналка)'"""
    cursor.execute(query)
    db.commit()