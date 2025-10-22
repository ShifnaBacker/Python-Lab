str=input("Enter a string: ")
freq={}
for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Character frequency in the given string:",freq)