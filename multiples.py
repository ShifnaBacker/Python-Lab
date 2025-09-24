x=int(input("Enter the number: "))
y=int(input("Enter the limit: "))
print("First",y,"Multiples of",x)
for i in range(1,y+1):
    z=i*x
    print(z)