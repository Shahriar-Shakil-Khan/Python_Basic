'''
n=int(input("Enter Number := "))

for i in range(n+1):
    print(i*"*")
    
''' 
# Python code to print a pattern
n = int(input("Enter N = "))

for row in range(1, n+1):
    for col in range(1, row+1):
        print(col, end=" ")
    print()
   