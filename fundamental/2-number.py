import random

#number in python
x = 1    # int
y = 2.8  # float
z = 1j   # complex

#detect ho type data of variabel
print(type(x))
print(type(y))
print(type(z))

#covert variabel to other type number 

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c)) 

# random number , you must import
# import random 
print(random.randrange(1, 10)) #random number from 1 to 10