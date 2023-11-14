import sqlite3

conn = sqlite3.connect('ActBase1')

cursor = conn.cursor()

cursor.execute(''' CREATE TABLE IF NOT EXISTS usuarios (
    id INTERGER PRIMARY KEY, 
    nombre TEXT NOT NULL,
    edad INTERGER)''')

cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES (?, ?)',('Felipe', 20))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('Aelin',22))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('Alejandro',20))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('Esteban',20))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('Gerardo',20))
cursor.execute('INSERT INTO usuarios(nombre, edad)VALUES(?,?)', ('Daniel',23))

conn.commit()

cursor.execute('SELECT *FROM usuarios')
usuarios = cursor.fetchall()
    

print('Lista de usuarios: ')
for usuario in usuarios:
    print(usuario)
    
conn.close()



