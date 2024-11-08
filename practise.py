'''
x=10
y=5
print("sum = ",x+y)
print("sub = ",x-y)
print("mul = ",x*y)
print("div = ",x/y)

p=10j
print(type(p))
#print(" = ",x+y)

numbers=range(1,20,4)
numbers1=range(20)
print(*numbers1)

x={1,2,3,4,5}
print(x)
y={1,2,3,4,5,2,5}
print(y)

x=frozenset([1,2,3,4,5,6,1,2,3])
print(x)

student={
    'name':'Shakil',
    'age':'24',
    'last':'khan'
}
print(student.get('last_name',"Not a found"))
'''

#Immutable data type

'''
#int
x=10
first_location=id(x)
x=11
second_location=id(x)

print(first_location)
print(second_location)

'''
'''

#float
x=10.899
first_location=id(x)
x=11.876
second_location=id(x)

print(first_location)
print(second_location)

'''
'''
#string
x='Shakil'
first_location=id(x)
x='Nabil'
second_location=id(x)

print(first_location)
print(second_location)
'''
'''
#tuple
x=(1,2,3.98,'Shakil')
first_location=id(x)
x=(5,2.5,3.91,'Nabil')
second_location=id(x)

print(first_location)
print(second_location)
'''

'''
#frozenset
x=frozenset([1,5,3,7])
first_location=id(x)
x=frozenset([2,7,9,4])
second_location=id(x)

print(first_location)
print(second_location)
'''
'''
#int
x=10
first_location=id(x)
x=10
second_location=id(x)      # Here x =10 and x=10 so there is location not change and show same location

print(first_location)
print(second_location)
'''
'''
#Mutable data type
#list
l=["Shakil",1,2,3.7]
first_location=id(l)
print(first_location)
print()
l[0]="Nabil"
second_location=id(l)
print(l)
print(second_location)

'''
'''
#Dictionary
l={'101':'Shakil','102':'Nabil'}
first_location=id(l)
print(first_location)

l['101']='Khan'
second_location=id(l)
print(l)
print(second_location)
'''
'''
#Set
s={1,2,3,4}
first_location=id(s)
print(first_location)
print()

s.add(5)
second_location=id(s)
print(s)
print(second_location)
'''
'''
#type Conversion

a="123"

x=int(a)
print(x)

y=float(a)
print(y)

z=str(a)
print(z)
'''

'''
a="SHAKIL"
x=int(a)        # it is wrong and show error
print(x)
'''

'''
try:
    a = "SHAKIL"
    x = int(a)  # it is wrong and show error
    print(x)

except Exception as e:
    print(e)

'''
'''
number1=int(input("Enter first number : "))
number2=int(input("Enter second number : "))

result=number1+number2
print ("sum :",result)
result=number1-number2
print ("sub :",result)
result=number1*number2
print ("mul :",result)
result=number1/number2
print ("dev :",result)
result=number1%number2
print ("modolus :",result)
result=number1//number2
print ("Floor :",result)
'''
'''
name='shakil said, "Hi Man!" '
print(name)

name1="shakil said, 'Hi Man!' "
print(name1)
'''

