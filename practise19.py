'''
result=lambda:10+15
print(result())

result=lambda x,y:x+y
print(result(5,10))

'''

result=lambda x,y: x if x>y else y
print(result(5,10))
