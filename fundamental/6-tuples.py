#contoh tuples
"""
tuples bersifat ordered, tidak bisa berubah, dan dapat duplicate
"""
contoh = ("satu", "dua", "tiga", "tiga")
print(contoh)

#acces tuples
print(contoh[0])
print(contoh[-1])
print(contoh[1:4])

#loop tuples
for x in contoh:
    print(x)

#check if exist 
if "satu" in contoh:
    print("yes exist")

#length of tuples
print(len(contoh))

#kita tidak bisa menghapus element atau menambahkan element pada tuples
# tapi kita bisa delete tuples
del contoh  #delete tuples

#join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

#tuples constructor untuk membuat tuples
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)