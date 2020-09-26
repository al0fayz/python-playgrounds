file = open("new.txt", "x")
file = open("new.txt", "w")
file.write("its only test!")
file = open("new.txt", "r")
print(file.read())
file.close()

# delete file
import os
os.remove("new.txt")
