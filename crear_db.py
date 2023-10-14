import mysql.connector
mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="colegio" )
mycursor = mydb.cursor()

for i in range(1,10):
    archivos = "db0"+str(i) + ".sql" 
    if i == 1 or i == 9:
        f = open(archivos, "r")
        lineas = f.readlines()
        f.close()
        for query  in lineas:
            print(query)
            mycursor.execute(query)
        
    else:
        f = open (archivos,'r')
        query = f.read()
        f.close()
        print(query)
        mycursor.execute(query)
        
