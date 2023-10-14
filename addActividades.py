import os
import mysql.connector

def menu():
    print("1-Agregar alumno a actividad")
    print("2-Listas actividad con alumnos")
    print("3-salir")
    print("Selecciones una opcion")

def buscar(codigo, rut):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT * FROM `inscripcionesactividades` WHERE codigo = '"+codigo+"' AND rut_alumno = '"+rut+"'"
    mycursor.execute(query)
    datos1 = mycursor.fetchall()
    filas1 = mycursor.rowcount
    if( filas1 == 1):
        return (True, datos1)
    else:
        return (False, datos1)

def insertar(codigo,rut_alumno):
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "INSERT INTO `inscripcionesactividades` (`codigo`, `rut_alumno`)"
    query += " VALUES ('"+codigo+"', '"+rut_alumno+"');"
    mycursor.execute(query)
    mydb.commit()

def agregar():
    codigo = input("Ingrese codigo ")
    rut = input("Ingrese RUT alumno ")
    (existe, datos) = buscar(codigo, rut)
    if existe:
        print( "Codigo:", datos[0][0] )
        print( "RUT alumno:", datos[0][1] )
        print("Alumno ya esta agregado")
        print("Cualquiel otra  opcion volvera al menu")
        input()
        
    else:
        insertar(codigo,rut)
        print( "Agregando alumno")
        input()
        
        
    
def listar():
    mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
    mycursor = mydb.cursor()
    mycursor.execute("USE colegio;")
    query = "SELECT * FROM `inscripcionesactividades` WHERE 1;"
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