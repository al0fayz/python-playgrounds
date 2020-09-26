# file handling in python
f = open("test.txt", "rt")
#read file
# print(f.read()) #read all

# print(f.read(5)) # 5 character 
print(f.readline()) # only 1 line
f.close()