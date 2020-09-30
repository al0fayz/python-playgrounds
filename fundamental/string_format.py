#string format
"""
the format() use to certain string will you display as you expected
To control such values, add placeholders (curly brackets {}) in the text, and run the values through the format() method: 
this is use if we want to show a value from database to string.
"""
# example
price = 47
txt = "the price of domain is {} dollars"
print(txt.format(price))

#You can add parameters inside the curly brackets to specify how to convert the value:
contoh = "the price of domain is {:.2f} dollars" #look in {} that is format number into float
print(contoh.format(price))

#example multiple value
out = "{} and {} have some value , they get {:.2f} for mathematic excercise!"
name1 = "anna"
name2 = "budi"
val = 77
print(out.format(name1, name2, val))

#example with index in {}
age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))

#example with index key 
myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))