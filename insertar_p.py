import mysql.connector
mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
mycursor = mydb.cursor()
mycursor.execute("USE colegio;")
query = "INSERT INTO `personas` (`rut`, `nombre`, `apellido`, `direccion`) VALUES ('1234678-3', 'jorge', 'peñaloza', 'las castañas');"
mycursor.execute(query)
query = "INSERT INTO `personas` (`rut`, `nombre`, `apellido`, `direccion`) VALUES ('1234678-4', 'ana', 'valdez', 'las castañas');"
mycursor.execute(query)
mydb.commit()
print(mycursor.rowcount, "record inserted.")
