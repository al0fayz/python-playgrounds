import json

#Convert from JSON to Python:
# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

print("==============================================")
#Convert from Python to JSON:
# a Python object (dict):
c = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

# convert into JSON:
d = json.dumps(c)

# the result is a JSON string:
print(d)

print("==============================================")
#Convert Python objects into JSON strings, and print the values:
print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

#Convert a Python object containing all the legal data types:
ss = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(ss))
#indent use for easy to read
#separator use for change default separator
print(json.dumps(ss, indent=4, separators=(". ", " = ")))
"""
Use the sort_keys parameter to specify if the result should be sorted or not:
json.dumps(x, indent=4, sort_keys=True)
"""