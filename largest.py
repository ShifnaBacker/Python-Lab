x,y,z=map(int,input("Enter three numbers: ").split())
if x>y and x>z:
    print("Largest number is",x)
elif y>x and y>z:
    print("Largest number is",y)
else:
    print("Largest number is",z)