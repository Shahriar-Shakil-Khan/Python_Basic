number_of_word = 0
number_of_letter = 0
number_of_digit = 0

text= input("Please!enter text : ")

for number in text:
    number=number.lower()
    if number>="a" and number<="z":
       number_of_letter = number_of_letter +1
       
    
    elif number>="0" and number<="9":
        number_of_digit = number_of_digit +1
       
    
    elif number==" ":
       number_of_word = number_of_word +1
   

print(number_of_word+1)
print(number_of_letter)
print(number_of_digit)
       
    

