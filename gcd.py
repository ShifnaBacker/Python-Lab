a,b=map(int,input("Enter two numbers: ").split())
while b!=0:
    temp=b
    b=a%b
    a=temp
print("GCD is",a)