

#list

x=['Shakil','Nabil','Masud',1,3.14]
first_location=id(x)
print(first_location)

x[0]=4
second_location=id(x)
print(second_location)
print(x)

#Dictionary

x={'a':10,'b':20}
first_location=id(x)
print(first_location)

x['a']=4
second_location=id(x)
print(second_location)



#set
x={1,2,3,4,5}
print(x)
first_location=id(x)
print(first_location)
x.add(6)
print(x)
second_location=id(x)
print(second_location)

