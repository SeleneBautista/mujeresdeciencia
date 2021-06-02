import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (title, content, autor) VALUES (?, ?, ?)",
            ('Primer Post', 'Contenido del primer post', 'Miguel')
            )

cur.execute("INSERT INTO posts (title, content, autor) VALUES (?, ?, ?)",
            ('Segundo Post', 'Contenido del segundo post', 'Kathy')
            )

cur.execute("INSERT INTO posts (title, content, autor) VALUES (?, ?, ?)",
            ('Tercer Post', 'Contenido del tercer post', 'Yamili')
            )


connection.commit()
connection.close()

