file = open("newfile.txt", "x")
file.close()
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
# os.rmdir("folder_name")