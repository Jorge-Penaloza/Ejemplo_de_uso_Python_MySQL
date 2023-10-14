import os
import mysql.connector

def menu():
    print("1-Actualizar actividad")
    print("2-Listas actividad")
    print("3-salir")
    print("Selecciones una opcion")

def buscar(codigo):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT * FROM `actividad` WHERE codigo = '"+codigo+"'"
    mycursor.execute(query)
    datos1 = mycursor.fetchall()
    filas1 = mycursor.rowcount
    if( filas1 == 1):
        return (True, datos1)
    else:
        return (False, datos1)

def insertar(codigo,descripcion,planEstudios):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "INSERT INTO `actividad` (`codigo`, `descripcion`, `planEstudios`)"
    query += " VALUES ('"+codigo+"', '"+descripcion+"', '"+planEstudios+"');"
    mycursor.execute(query)
    mydb.commit()
    

def actualizar(codigo,descripcion,planEstudios):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "UPDATE `actividad` SET `descripcion` = '"+descripcion+"', `planEstudios` = '"+planEstudios
    query += "' WHERE `actividad`.`codigo` = '"+codigo+"';"
    mycursor.execute(query)
    mydb.commit()

def eliminar(codigo):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "DELETE FROM `actividad` WHERE `actividad`.`codigo` = \'"+codigo+"\'"
    mycursor.execute(query)
    mydb.commit()
 
def agregar():
    codigo = input("Ingrese codigo ")
    (existe, datos) = buscar(codigo)
    if existe:
        print( "Codigo:", datos[0][0] )
        print( "Descripción:", datos[0][1] )
        print( "Plan de estudios:", datos[0][2] )
        
        print("Actividad ya existe")
        print("1-Actualizar informacion de actividad")
        print("2-Eliminar informacion de actividad")
        print("Cualquiel otra  opcion volvera al menu")
        try: 
            op = int(input())
        except:
            op = 0
        if op == 1:
            print( "Descripción")
            descripcion = input()
            print( "Plan de estudios")
            planEstudios = input()
          
            actualizar(codigo,descripcion,planEstudios)
        if op == 2:
            eliminar(codigo)
    else:
        print("Actividad no existe, si desea agregarla ingrese los datos")
        print("De lo contrario presione enter en los demas campos sin ingresar informacion")
        print( "Descripción")
        descripcion = input()
        print( "Plan de estudios")
        planEstudios = input()
        if(codigo == "" or descripcion == "" or planEstudios == ""):
            pass
        else:                
            insertar(codigo,descripcion,planEstudios)
    
def listar():
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT * FROM `actividad` WHERE 1;"
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