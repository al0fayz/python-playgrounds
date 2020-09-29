#example array in python
arr = ["satu", "dua", "tiga"]
print(arr[0])

#length of array
sum = len(arr)
print(sum)

#loops with array
for x in arr:
    print(x)

#adding elements to array
arr.append("empat")
print(arr[len(arr) - 1]) #return last value


#removing array elements
arr.pop(1)

#or 
arr.remove("empat")
for x in arr:
    print(x)