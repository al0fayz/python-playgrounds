#example class in python
class siswa:
    #this like constructor in other programming
    def __init__(self, name, city):
        #this like this in other language 
        self.name = name
        self.city = city

#create object
siswa_object = siswa("bento", "Jakarta")
print(siswa_object.name)
print(siswa_object.city)

#modify object 
siswa_object.name = "alfa code"
print(siswa_object.name)

#delete properties
del siswa_object.city

#delete object
del siswa_object