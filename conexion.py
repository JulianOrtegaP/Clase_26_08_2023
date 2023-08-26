import sqlite3  #paso1 importar SQLITE3 - conectar SQLI con python
conexion = sqlite3.connect("sistema_cursos.db")  # creamos un canal para conectar la bd con python
print(conexion) #Verificamos la conexion
cursor = conexion.cursor() #cursor es una herramienta para crear consultas
#cursor.execute("DROP TABLE IF EXISTS cursos")
#cursor.execute("CREATE TABLE cursos (id INTEGER PRIMARY KEY AUTOINCREMENT ,nombre TEXT ,duracion INTEGER ,cupos INTEGER ,activo BOOLEAN)") #Ahora que hemos configurado una conexión y un cursor, podemos crear una tabla cursos con las columnas title,

#GUARDAR CURSO

"""cursor.execute('''
INSERT INTO cursos(nombre,duracion,cupos,activo)
VALUES('Fundamentos 2',2,30,True)
               ('JAVA',2,30,True),
               ('JAVA',2,30,True),             
)
conexion.commit()

#LISTAR TODO

respuesta = cursor.execute("SELECT * FROM cursos")
info = respuesta.fetchall()
print(info)



#BUSCAR UNO

datos = cursor.execute("SELECT * FROM cursos WHERE nombre = 'Fundamentos 1'")
info = datos.fecthone()
print(info)



#MODIFICAR
cursor.execute("UPDATE cursos SET nombre = 'Practica Formativa',duracion=1 WHERE id = 2")
conexion.commit()

"""

#ELIMINAR

cursor.execute("DELETE FROM cursos WHERE id =3")
conexion.commit()
