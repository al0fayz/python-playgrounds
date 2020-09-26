import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python_example"
)

con = db.cursor()
con.execute("SELECT * FROM customers")

myresult = con.fetchall()

for x in myresult:
  print(x)


print("==========================================")
# select column 
con.execute("SELECT name, address FROM customers")
myresult = con.fetchall()

for x in myresult:
  print(x)

print("==========================================")
#get 1 row
con.execute("SELECT * FROM customers")

myresult = con.fetchone()

print(myresult) 