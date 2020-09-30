#insert another python file to python 
example:
we have python with name ```mymodule.py``` with code like this:
```
def hello():
    print("hello all!")

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

and i will call on my python is like this:
```
import mymodule
#run function
mymodule.hello()
a = mymodule.person1["age"]
print(a)
```