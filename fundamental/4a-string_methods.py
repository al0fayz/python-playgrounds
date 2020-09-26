# get character in string

name = "alfa code"
print(name[1])

#slicing 
print(name[2:5])

# negative indexing
print(name[-5:-2])


#string length
print("length of name is:", len(name))

#strip() 
#is remove first and end whitesspace on string
example = " hello world "
print(example)

print("if use strip:")
print(example.strip())

#lower
print(name.lower())

#upper 
print(name.upper())

#replace 
print(name.replace("a", "e"))

#split 
print(name.split(" "))

#check string
x = "alfa" in name
print(x)

# not 
y = "a" not in name 
print(y)

#concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)

#format 
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))