file = open("test.txt", "w")
file.write("hello all this is new content!")

file = open("test.txt", "r")
print(file.read())

file.close()