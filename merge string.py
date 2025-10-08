s1=input("Enter first string: ")
s2=input("Enter second string: ")
if len(s1)<2 or len(s2)<2:
    print("Strings should have atleast two characters")
else:
    str1=s1[0]+s2[1]+s1[2:]
    str2=s2[0]+s1[1]+s2[2:]
s3=str1+str2
print("New string is",s3)