import mysql.connector
mydb = mysql.connector.connect( host="127.0.0.1", user="root", password="",database="test" )
mycursor = mydb.cursor()
db = []
db.append("CREATE DATABASE IF NOT EXISTS colegio;")
db.append("USE colegio;")
query = "CREATE TABLE IF NOT EXISTS `colegio`.`estudiantes`"
query += "( `rut` TEXT NOT NULL , `nombre` VARCHAR(255) NOT NULL ,"
query += " `apellido` VARCHAR(255) NOT NULL ,"
query += " `direccion` VARCHAR(255) NOT NULL ,"
query += " UNIQUE `rut_i` (`rut`(10))) "
query += "ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;"
db.append(query)
query = "CREATE TABLE IF NOT EXISTS `colegio`.`apoderados`"
query += "( `rut` TEXT NOT NULL , `nombre` VARCHAR(255) NOT NULL ,"
query += " `apellido` VARCHAR(255) NOT NULL ,"
query += " `direccion` VARCHAR(255) NOT NULL ,"
query += " UNIQUE `rut_i` (`rut`(10))) "
query += "ENGINE = InnoDB CHARSET=utf8mb4 COLLATE utf8mb4_general_ci;"
db.append(query)
for sentencia in db:
    mycursor.execute(sentencia)
