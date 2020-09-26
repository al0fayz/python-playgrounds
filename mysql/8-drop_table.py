import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="python_example"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

# delete directly
mycursor.execute(sql) 
print("deleted!")

# delete if table exist
sql = "DROP TABLE IF EXISTS customers"
mycursor.execute(sql) 