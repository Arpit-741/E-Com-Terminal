import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Arpit91755@"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE my_database")