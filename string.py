s=input("Enter a string: ")
if len(s)<=1:
    new_s=s
else:
    new_s=s[-1]+s[1:-1]+s[0]
print("String after swapping first and last letters is",new_s)
