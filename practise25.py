'''
try:
    result=10/0
    print(result)

except ZeroDivisionError:
    print(" ZeroDivisionError")

'''

try:
    with open("new.text","r") as file:
        content=file.read()
        result=10/int(content)
        print(result)

except Exception as e:
    print(e)

