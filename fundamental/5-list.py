#example list
"""
list seperti array
list bersifat ordered, dapat berubah, dan dapat duplicate
"""
ex = ["apple", "banana", "cherry"]
print(ex)

#access list 
print(ex[1])

#negative indexing
print(ex[-1])

#range indexing
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:4])
print(thislist[2:])
print(thislist[-4:-1])

#change item value
thislist[1] = "ayam goreng"
print(thislist)

# loop in list 
for x in thislist:
    print(x)

#check item is exist 
if "apple" in thislist:
    print("yes exist!")

#length list 
print(len(thislist))

#add item end of list
thislist.append("becak")

#change specific item 
thislist[4] = "motor"

# remove item 
thislist.remove("motor")

print(thislist)

#pop => delete last index
thislist.pop()
print(thislist)

#del =>delete specified index
del thislist[0]
print(thislist)

# del list ex; del <list_name>

#clear =>empty the list
thislist.clear()
print(thislist)

#copy list to other list
cth = ["hello", "anna"]
ch = cth.copy()
#or
# ch = list(cth)    #this is some like copy
print(ch)

#join a list 
list1 = ["a", "b", "c", "d"]
list2 = [1, 2, 3, 4]
#cara 1 
list3 = list1 + list2
"""
#cara 2 
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
"""

"""
#cara 3 menggunakan extend()
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)
"""
print(list3)

#pembuatan list dengan list constructor
cth_list = list(("apple", "banana", "apple"))
print(cth_list)