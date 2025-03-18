'''
def say_hello():
    print("Hello World! 1")
    print("Hello World! 2")

say_hello()
say_hello()
say_hello()

def addTwo(a,b):
    num1=a
    num2=b
    print(num1+num2)

addTwo(10,30)

addTwo(1,3)

addTwo(10,40)
addTwo(100,400)


def addTwo(a,b=300):
    num1=a
    num2=b
    print(num1+num2)

addTwo(100,50)



def tuples(*numbers):
    #print(numbers)
    for x in numbers:
        print(x)


tuples(50,30,40,"Shakil",10+10j)

'''


def dict(**information):
    #print(information)
    #print(information['name'])
    for key,value in information.items():
        print(f"{key}: {value}")


dict(
    name="Shakil",
    age="34",
    city="Dhaka"

)











