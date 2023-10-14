import os
import mysql.connector

def menu():
    print("1-Actualizar apoderado")
    print("2-Listas apoderados")
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
    query = "SELECT * FROM `apoderados` WHERE rut = '"+rut+"'"
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

def insertar(rut,nombre,apellido, direccion, rut_a):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "INSERT INTO `personas` (`rut`, `nombre`, `apellido`, `direccion`)"
    query += " VALUES ('"+rut+"', '"+nombre+"', '"+apellido+"','"+direccion+"');"
    mycursor.execute(query)
    mydb.commit()
    query = "INSERT INTO `apoderados` (`rut`, `rut_alumno`) VALUES ('"+rut+"', '"+rut_a+"');"
    print(query)
    mycursor.execute(query)
    mydb.commit()

def actualizar(rut,nombre,apellido, direccion, rut_a):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "UPDATE `personas` SET `nombre` = '"+nombre+"', `apellido` = '"+apellido
    query += "', `direccion` = '"+direccion+"' WHERE `personas`.`rut` = '"+rut+"';"
    mycursor.execute(query)
    mydb.commit()
    query = "UPDATE `apoderados` SET `rut_alumno` = '"+rut_a+"' WHERE `apoderados`.`rut` = '"+rut+"';"
    mycursor.execute(query)
    mydb.commit()

def eliminar(rut):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "DELETE FROM `apoderados` WHERE `apoderados`.`rut` = \'"+rut+"\'"
    mycursor.execute(query)
    mydb.commit()
    query = "DELETE FROM `personas` WHERE `personas`.`rut` = \'"+rut+"\'"
    mycursor.execute(query)
    mydb.commit()
def agregar():
    rut = input("Ingrese RUT ")
    (existe, datos, rut_a) = buscar(rut)
    if existe:
        print( "RUT:", datos[0][0] )
        print( "Nombre:", datos[0][1] )
        print( "Apellido:", datos[0][2] )
        print( "Direccion:", datos[0][3] )
        print( "Rut alumno:", rut_a )
        print("persona ya existe")
        print("1-Actualizar informacion de apoderado")
        print("2-Eliminar informacion de apoderado")
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
            print( "Rut alumno")
            rut_a = input()
            actualizar(rut,nombre,apellido,direccion,rut_a)
        if op == 2:
            eliminar(rut)
    else:
        print("apoderado no existe, si desea agregarlo ingrese los datos")
        print("De lo contrario presione enter en los demas campos sin ingresar informacion")
        print( "Nombre")
        nombre = input()
        print( "Apellido")
        apellido = input()
        print( "Direccion")
        direccion = input()
        print( "Rut alumno")
        rut_a = input()
        if(nombre == "" or apellido == "" or direccion == "" or rut_a == 0 ):
            pass
        else:                
            insertar(rut,nombre,direccion,apellido, rut_a)
    
def listar():
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT a.rut, p.nombre, p.apellido, p.direccion, e.rut FROM apoderados as a "
    query += "LEFT JOIN personas AS p ON a.rut = p.rut LEFT JOIN estudiantes as e ON e.rut = a.rut_alumno;"
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