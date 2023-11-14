import sqlite3

conn = sqlite3.connect('ActBase1')

cursor = conn.cursor()

cursor.execute('UPDATE usuarios SET edad=? WHERE nombre=?',(22, ' jorge'))
conn.commit()

cursor.execute('SELECT *FROM usuarios')
usuarios = cursor.fetchall()

print('Lista de usuarios: ')
for usuario in usuarios:
    print(usuario)
    
conn.close()
