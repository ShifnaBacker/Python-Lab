str=input("Enter a String: ")
if len(str) >=3:
    if str.endswith("ing"):
        str += "ly"
    else:
        str += "ing"
    print("Modified String is",str)
else:
    print("String is too short!")
