#lambda argument:expression
#print((lambda x,y : x+y)(5,4))

#a=(lambda x,y : x*x + 2*x*y + y*y)
#print(a(2,3))

def myfunc(n):
    return lambda a:a*n

myfun=myfunc(2)
print(myfun(11))

    