
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for Item,element in thisdict.items():
    print("{}:{}".format(Item,element))


x={1,2,3,4,5,6,7,8,9}
for numbers in x:
    print(numbers)


for x in range(1,20,2):
    print(x)



for y in range(1,15):
    if y==10:
        break
    print(y)


for z in range(1,10):
    if z==4:
        continue
    print(z)


x="bangladesh"

for d in x:
    x=x+1
    print(d)