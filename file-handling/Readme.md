File handling
=============
"r" - Read - Default value. Opens a file for reading, error if the file does not exist

"a" - Append - Opens a file for appending, creates the file if it does not exist

"w" - Write - Opens a file for writing, creates the file if it does not exist

"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode:
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)

example
========
1. open file and read
```
file = open("test.txt", "r")
#show all
print(file.read())

#show only character
print(file.read(6))

# show 1 line 
print(file.readline())
```
2. open file and write
note:
-> "a" - Append - will append to the end of the file

-> "w" - Write - will overwrite any existing content
```
# write
file = open("test.txt", "w")
file.write("hello all this new content!")

file = open("test.txt", "r")
print(file.read())

# append
file = open("test.txt", "a")
file.write("this add with append!")

file = open("test.txt", "r")
print(file.read())

# new file
file = opne("newfile.txt", "x")
```

3. delete  file
```
#delete file
import os 
os.remove("newfile.txt")
print("success delete!")

# remove file check first
f = open("A.txt", "x")
f.close()

if os.path.exists("A.txt"):
    os.remove("A.txt")
    print("success delete file!")
else:
    print("file not exist")

#remove folder
os.rmdir("folder_name")
```