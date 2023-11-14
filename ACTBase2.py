import sqlite3

conn = sqlite3.connect('ActBase1')

cursor = conn.cursor()

cursor.execute('DELETE FROM usuarios WHERE nombre=?', ('Daniel',))
conn.commit()

cursor.execute('SELECT *FROM usuarios')
usuarios = cursor.fetchall()

print('Lista de usuarios: ')
for usuario in usuarios:
    print(usuario)
    
conn.close()
