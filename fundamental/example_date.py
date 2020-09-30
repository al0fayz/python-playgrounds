import datetime
now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%A"))


#creating date 
x = datetime.datetime(2020, 5, 17)

print(x)
print(x.strftime("%B"))