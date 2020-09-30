import os
#example exception handling
try:
    print(x)
except:
    print("something have error!")
finally:
    print("example try catch in python") #The finally block, if specified, will be executed regardless if the try block raises an error or not.

#other example
try:
    f = open("demofile.txt", "x")
    f.write("hello world")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()
  os.remove("demofile.txt")

#raise exception 
# add exception 
x = -1
if x < 0:
    raise Exception("x is lessthan 0")

#other example 
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")