import os
import estudiantes
import apoderados
import actividades
import asignaturas
import addAsignaturas
import addActividades

def menu():
    print("1-Estudiantes")
    print("2-Apoderados")
    print("3-Asignaturas")
    print("4-Actividades")
    print("5-Agregar alumno a asignaturas")
    print("6-Agregar alumno a actividades")
    print("7-salir")
    print("Selecciones una opcion")

op = 0
while( op != 7):
    os.system ("cls") 
    menu()
    op = int(input())
    if op == 1:
        estudiantes.principal() 
    if op == 2:
        apoderados.principal ()
    if op == 3:
        asignaturas.principal()
    if op == 4:
        actividades.principal()
    if op == 5:
        addAsignaturas.principal()
    if op == 6:
        addActividades.principal()