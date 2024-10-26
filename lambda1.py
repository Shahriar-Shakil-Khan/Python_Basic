def math(n):
    return lambda a: a*n

x=math(10)
print(x(6))



def math1(n):
    return lambda a: a*n

y=math1(5)
z=math1(10)

print(y(4))
print(z(3))

