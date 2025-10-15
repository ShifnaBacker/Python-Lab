dict={}
keys=int(input("Enter the number of keys in the dictionaries: "))
for i in range(keys):
    key=input("Enter the key : ")
    value=input("Enter the value :")
    dict[key]=value
print("Dictionary: ",dict)
keys=[]
for k in dict:
    keys.append(k)
n=len(keys)
for i in range (n-1):
    for j in range (0,n-i-1):
        if keys[j]>keys[j+1]:
            keys[j],keys[j+1]=keys[j+1],keys[j]
sorted_dict={}
for k in keys:
    sorted_dict[k]=dict[k]
print("Sorted dictionary: ",sorted_dict)

