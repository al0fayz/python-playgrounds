#example inheritance 
"""
    Inheritance allows us to define a class that inherits all the methods and properties from another class.

    Parent class is the class being inherited from, also called base class.

    Child class is the class that inherits from another class, also called derived class.

"""
#parent class 
class person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name  = last_name

    def say(self):
        print("hello "+ self.first_name + " " + self.last_name)

#create object
orang = person("joko", "warjono")
orang.say()

#inheritance to child class 
class siswa(person):
    #Use the pass keyword when you do not want to add any other properties or methods to the class.
    pass


#create object siswa
sw = siswa("bejo", "anak deso")
sw.say()

#inheritance to child with add init and method 
class dosen(person):
    def __init__(self, first_name, last_name, teaching):
        #if you not add super() init parent will be overide by init child 
        #seuper() use for keep init, method and properties on the parents
        super().__init__(first_name, last_name)
        self.teaching = teaching

    def welcome(self):
        print("welcome "+ self.first_name + " "+ self.last_name +" will teaching:"+ self.teaching)

ds = dosen("alfa", "code", "Hacker")
ds.welcome()