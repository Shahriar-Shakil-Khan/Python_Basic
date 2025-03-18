#large number compare 3 Number
''''
#num1=100
##num2=2000
#num3=30

num1=float(input("Enter number1 As you wish : "))
num2=float(input("Enter number2 As you wish : "))
num3=float(input("Enter number3 As you wish : "))

if num1>num2:
    if num1>num3:
        print("large= ",num1)
    else:
        print("larger=",num3) 
        
if num2>num1:
    if num2>num3:
        print("large= ",num2)
    else:
        print("larger=",num3)            
        
'''
#num1=100
##num2=2000
#num3=30

num1=float(input("Enter number1 As you wish : "))
num2=float(input("Enter number2 As you wish : "))
num3=float(input("Enter number3 As you wish : "))

if num1<num2:
    if num1<num3:
        print("smaller= ",num1)
    else:
        print("Smaller=",num3) 
        
if num2<num1:
    if num2<num3:
        print("Smaller= ",num2)
    else:
        print("Smaller=",num3)            