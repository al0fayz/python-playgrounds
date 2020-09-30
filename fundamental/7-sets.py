#set 
"""
set adalah collection /array yang mana unordered dan unindexed, dan tidak bisa duplicate artinya jika kamu menmbahkan data yang sudah ada 
maka akan di abaikan
arti dari pernyataan di atas adalah 
kamu tidak bisa menampilkan data set dengan cara 
thisset[0] ini akan error
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

#cara menampilkan data dengan loop
for x in thisset:
    print(x)

#check apakah ada 
print("banana" in thisset)

#menambah data 
thisset.add("orange")

print(thisset)

thisset.update(["orange", "mango", "grapes"])

print(thisset)

#length of set 

print(len(thisset))

#hapus data
thisset.remove("banana") #atau bisa menggunakan:  thisset.discard("banana")

print(thisset)

#mengkosongkan set

thisset.clear()

print(thisset)

#hapus set
del thisset

#menggabungkan set 
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

#atau
setA = {"a", "b" , "c"}
setB = {1, 2, 3}

setA.update(setB)
print(setA)

#set constructor
iniset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(iniset)