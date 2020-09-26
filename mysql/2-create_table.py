import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_example"
)

mycursor = mydb.cursor()
# create table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#show all table
mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x) 
# add column
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY") 
