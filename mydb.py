import mysql.connector

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password123",

)

# prepare a cursor object

cursorObject = dataBase.cursor()

# Create Database

cursorObject.execute("CREATE DATABASE zEleceed")

print('YAAAAAY')
