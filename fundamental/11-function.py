#example function 
def hello():
    print("hello all!")

#call the function
hello()

# function with parameter
def say(name, age):
    print("hello my name", name)
    print("and my ages", age)

say("alfa", 17)

#If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

#keyword
def my_function1(child3, child2, child1):
  print("The youngest child is " + child3)

my_function1(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

#If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
#This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function2(**kid):
  print("His last name is " + kid["lname"])

my_function2(fname = "Tobias", lname = "Refsnes")