import math
a,b,c=map(int,input("Enter the value of a,b,c in the quadratic equation: ").split())
d=(b*b)-(4*a*c)
e=math.sqrt(d)
if d>0:
    r1=(-b+e)/(2*a)
    r2=(-b-e)/(2*a)
    print("The roots are",r1,"and",r2)
elif d==0:
    r1=-b/(2*a)
    print("The root is",r1)
else:
    print("The roots are not real")