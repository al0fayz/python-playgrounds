import mysql.connector

#create database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
koneksi = db.cursor()
koneksi.execute("CREATE DATABASE python_example")
#show all database
koneksi.execute("SHOW DATABASES")
for x in koneksi:
    print(x)