#print((lambda a,b:a+b)(1,2)) # simply

'''
math=lambda x,y,z: x*x + y*y +z*z
print(math(2,2,2))                       
'''

'''
math=lambda x,y,z: x*x + y*y +z*z
x=math(2,3,1)
print("ans = ",x)
'''
'''
def math(x,y):
    return lambda x,y:x+y

a=math(1,2)
print(a(1,2))
'''

def math(x,y):
    return lambda x,y:x+y
print(math(1,2)(1,2))



