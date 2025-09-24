N = int(input("Enter the number of squares to be printed: "))
squares = [x**2 for x in range(1,N+1)]
print("Squares:",squares)