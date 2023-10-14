import os
import mysql.connector

def menu():
    print("1-Actualizar estudiante")
    print("2-Listas estudiantes")
    print("3-salir")
    print("Selecciones una opcion")

def buscar(rut):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT * FROM `personas` WHERE rut = '"+rut+"'"
    mycursor.execute(query)
    datos1 = mycursor.fetchall()
    filas1 = mycursor.rowcount
    query = "SELECT * FROM `estudiantes` WHERE rut = '"+rut+"'"
    mycursor.execute(query)
    datos2 = mycursor.fetchall()
    filas2 = mycursor.rowcount
    if filas2 == 1:
        an = datos2[0][1]
    else:
        an = ""
    if( filas1 == 1):
        return (True, datos1, an)
    else:
        return (False, datos1, an)

def insertar(rut,nombre,apellido, direccion,anio):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "INSERT INTO `personas` (`rut`, `nombre`, `apellido`, `direccion`)"
    query += " VALUES ('"+rut+"', '"+nombre+"', '"+apellido+"','"+direccion+"');"
    mycursor.execute(query)
    mydb.commit()
    query = "INSERT INTO `estudiantes` (`rut`, `anio`) VALUES ('"+rut+"', '"+anio+"');"
    mycursor.execute(query)
    mydb.commit()

def actualizar(rut,nombre,apellido, direccion, anio):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "UPDATE `personas` SET `nombre` = '"+nombre+"', `apellido` = '"+apellido
    query += "', `direccion` = '"+direccion+"' WHERE `personas`.`rut` = '"+rut+"';"
    mycursor.execute(query)
    mydb.commit()
    query = "UPDATE `estudiantes` SET `anio` = '"+anio+"' WHERE `estudiantes`.`rut` = '"+rut+"';"
    mycursor.execute(query)
    mydb.commit()

def eliminar(rut):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "DELETE FROM `estudiantes` WHERE `estudiantes`.`rut` = \'"+rut+"\'"
    mycursor.execute(query)
    mydb.commit()
    query = "DELETE FROM `personas` WHERE `personas`.`rut` = \'"+rut+"\'"
    mycursor.execute(query)
    mydb.commit()
def agregar():
    rut = input("Ingrese RUT ")
    (existe, datos, anio) = buscar(rut)
    if existe:
        print( "RUT:", datos[0][0] )
        print( "Nombre:", datos[0][1] )
        print( "Apellido:", datos[0][2] )
        print( "Direccion:", datos[0][3] )
        print( "Año:", anio )
        print("Estudiante ya existe")
        print("1-Actualizar informacion de estudiante")
        print("2-Eliminar informacion de estudiante")
        print("Cualquiel otra  opcion volvera al menu")
        try: 
            op = int(input())
        except:
            op = 0
        if op == 1:
            print( "Nombre")
            nombre = input()
            print( "Apellido")
            apellido = input()
            print( "Direccion")
            direccion = input()
            print( "Año")
            anio = input()
            actualizar(rut,nombre,apellido,direccion,anio)
        if op == 2:
            eliminar(rut)
    else:
        print("Estudiante no existe, si desea agregarlo ingrese los datos")
        print("De lo contrario presione enter en los demas campos sin ingresar informacion")
        print( "Nombre")
        nombre = input()
        print( "Apellido")
        apellido = input()
        print( "Direccion")
        direccion = input()
        print( "Año")
        anio = input()
        if(nombre == "" or apellido == "" or direccion == "" or anio == 0 ):
            pass
        else:                
            insertar(rut,nombre,direccion,apellido, anio)
    
def listar():
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT `personas`.`rut` AS 'RUT', `personas`.`nombre` AS 'Nommbre',"
    query += " `personas`.`apellido` AS 'Apellido', `personas`.`direccion` AS 'Direccion', "
    query += "`estudiantes`.`anio` AS 'Anio' FROM `personas` LEFT JOIN `estudiantes` ON `personas`.`rut` = `estudiantes`.`rut`"
    query += "WHERE `estudiantes`.`anio` > 0"
    mycursor.execute(query)
    datos = mycursor.fetchall()
    for elemento in datos:
        print(elemento)
    input("Presione tecla para continuar")
    
def principal():
    op = 0
    while( op != 3):
        os.system ("cls") 
        menu()
        op = int(input())
        if op == 1:
            agregar()  
        if op == 2:
            listar()  