i=1
while i<=10:
    print('Bangladesh')
    i=i+1

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

index=0
Item=list(thisdict.items())
while index<len(Item):
    key,value=Item[index]
    print("{} : {}".format(key,value))
    index=index+1

x=['A','B','C',1,2,3]
index=0
while index<len(x):
     print(x[index])
     index=index+1

