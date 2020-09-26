#example variabel in python 
x = 5
y = 2
kalimat = "hello world"
kalimat1 = 'hai all!'

print(x)
print(y)
print(kalimat)
print(kalimat1)

a , b , c = 1, 2, 3
text1, text2, text3 = "apa", "kabar", "indonesia?"

print(a, b, c)
print(text1, text2, text3)

result1 = result2 = result3 = 80
print(result1, result2, result3)

print("your weight is" , result1) #integer
print("i like " + text3) #string

#example global variabel 
# this is a global variabel
name = "alfa" 
def test():
    # i can call variabel global inside function
    print("my name is " + name)

#call function
test()
# global variabel can call inside or outside function


# example local varibel 
def coba():
    address = "jakarta" #this is local variabel you can call on outside func
    print(address)
    # if you want set global varibel inside  function you can add global 
    #ex :
    global bahasa #you must defined first , you can't insert value directly
    bahasa = "indonesia"
    print(bahasa)

coba()
# i try call variabel global 
print("my language is "+ bahasa)
