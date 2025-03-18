
ch=str(input("Enter any cheracter : "))

if ch=="a" or ch=="e" or ch=="i" or ch=="o" or ch=="u" or ch=="A" or ch=="E" or ch=="I" or ch=="O" or ch=="U" :
 print("Yes Vowel")
else:
    print("Consonant") 


num=int(input("Enter any number : "))

if num%2==0 :
    print("Even")
else:
    print("Odd")

 
#leap year
year=int(input("Enter any Year : "))

if year%4==0 and year%100!=0 :
    print("This year is leap year")
elif year%400==0 :
    print("This year is leap year")
else:
    print("This year is not leap year")
       
