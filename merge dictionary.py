dict1={}
dict2={}
keys=int(input("Enter the number of keys for both dictionaries: "))
print("First dictionary ")
for i in range(keys):
    key=input("Enter the key : ")
    value=input("Enter the value :")
    dict1[key]=value

print("\nSecond Dictionary ")
for i in range(keys):
    key=input("Enter the key :")
    value=input("Enter the value :")
    dict2[key]=value

print("\nFirst dictionary: ",dict1)
print("Second dictionary: ",dict2)
merged=dict1 | dict2
print("Merged dictionary: ",merged)


