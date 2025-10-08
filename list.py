numbers = list(map(int,input("Enter some numbers: ").split()))
numbers_new= [num for num in numbers if num%2!=0]
print("Numbers withut even numbers are",numbers_new)