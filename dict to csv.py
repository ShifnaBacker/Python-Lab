import csv

mydict = [
    {"first": "Harry", "last": "Potter"},
    {"first": "Ron", "last": "Weasely"}, 
    {"first": "Hermione", "last": "Granger"}
]

with open("new.csv","w",newline="") as file:
    write = csv.DictWriter(file,fieldnames=["first","last"])
    write.writeheader()
    write.writerows(mydict)

with open("new.csv","r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
        