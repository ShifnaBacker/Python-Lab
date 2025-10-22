n=int(input("Enter the number of terms: "))
print("First",n,"terms of fibonacci series are: ")
f1,f2=0,1
for i in range(n):
    print(f1)
    f3=f1+f2
    f1=f2
    f2=f3
    