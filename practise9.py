#immutable


#int
x=10
first_location=id(x)
x=11
second_location=id(x)

print(first_location)
print(second_location)


#float
x=10.01
first_location=id(x)
x=11.10
second_location=id(x)

print(first_location)
print(second_location)

#str

x='Shakil'
first_location=id(x)
x='Nabil'
second_location=id(x)

print(first_location)
print(second_location)


#tuples

x=('Shakil','Nabil','Masud',1,3.14)
first_location=id(x)

x=('Shakil','Nabil','Masud',3.14)
second_location=id(x)

print(first_location)
print(second_location)



x=frozenset([1,2,3])
first_location=id(x)

x=frozenset([1,2,3,4])
second_location=id(x)

print(first_location)
print(second_location)