import datetime
x=datetime.datetime.now().year
y=int(input("Enter a year in future: "))
print("Leap years between",x,"and",y,"are")
for i in range(x,y+1):
    if(i % 4 == 0 and i % 100 != 0) or (i % 400 == 0):
        print(i)


