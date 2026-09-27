import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Arpit91755@",
    database = "e_com"
)

mycursor = mydb.cursor()

