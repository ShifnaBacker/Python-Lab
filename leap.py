x=int(input("Enter a year: "))
if x % 400 == 0:
    print(x,"is a leap year")
elif x % 100 == 0:
    print(x,"is a not leap year")
elif x % 4 == 0:
    print(x,"is a leap year")
else:
    print(x,"is a not leap year")