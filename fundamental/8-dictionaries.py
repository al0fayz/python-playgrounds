#dictionary di python
"""
A dictionary is a collection which is unordered, changeable and indexed. 
In Python dictionaries are written with curly brackets, and they have keys and values.
"""
#contoh:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#acces dictionary
print(thisdict["model"]) 
#atau
print(thisdict.get("model"))

#update value
thisdict["year"] = 2018
print(thisdict)

#loop in dictionary
for x in thisdict:
    print(x, " => ", thisdict[x])

#atau
print("=======================")
for x in thisdict.values():
  print(x)

#atau
print("=======================")
for x, y in thisdict.items():
  print(x, y)

#check if key is exist
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#length of dictionary
print(len(thisdict))

#tambah item
thisdict["color"] = "red"
print(thisdict)

#remove item
thisdict.pop("model")
print(thisdict)

#atau
# thisdict.popitem()        //ini delete last item
#atau 
#del thisdict["model"]     //ini sama 

#mengkosongkan dictionary
thisdict.clear()
print(thisdict)

#delete dictionary
del thisdict