'''
x=["Apple","cherry",1,"Banana","cherry",1,2.5,10+11j]
print(type(x))
print(len(x))
x.append("Shakil")
print(x)


list=['A','B','C','D','E']
print(list)
list.insert(0,"orrange")
print(list)

x=['A','B','C','D','E']
y=["apple", "banana", "cherry"]
#x.extend(y)
#print(x)
y.extend(x)
print(y)

x=['A','B','C','D','E']
x.remove('A')
print(x)

x=['A','B','C','D','A','E']
x.remove('A')
print(x)

x=['A','B','C','D','A','E']
x.pop(2)
print(x)

x=['A','B','C','D','A','E']
del x[0]
print(x)
'''
x=['A','B','C','D','A','E']
x.clear()
print(x)