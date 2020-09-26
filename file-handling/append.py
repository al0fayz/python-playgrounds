file = open("test.txt", "a")
file.write("this add with append!")

file = open("test.txt", "r")
print(file.read())

file.close()