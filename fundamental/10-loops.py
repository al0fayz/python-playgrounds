#example loops in python 
#1. while 
i = 1
while i < 10:
    print("angka", i)
    if(i == 7):
        break
    i += 1

x = 10
while x <= 100:
    print(x)
    x += 2
    if(x == 50):
        continue

#2. for
fruits = ["aple", "orange", "banana"]
for x in fruits:
    print(x)

#example range() default starting in 0
for x in range(10):
    print(x)

#using starter in range(start, end)
for x in range(2, 6):
    print(x)
# you can increment with other number by default is 1 in range
for v in range(2, 10, 2):
    print(v)