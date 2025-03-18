'''
def fun(a,b):
    num1=a
    num2=b
    sum=  num1 + num2
    sub = num1 - num2
    div = num1 / num2
    mul = num1 * num2

    return sum,sub,div,mul


math=fun(6,3)
print(math)

'''

def first_even_numbers(numbers):
    for number in numbers:
        if number % 2==0:
            return number

    return None

result=first_even_numbers([1,3,4,5,6,7,8,9,10])
print(result)




















