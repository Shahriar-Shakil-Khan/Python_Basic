
fruits=["Apple","Mangoo","Grap","Orrange","Banana"]
fruits.remove("Orrange")
print(fruits)

######################(in the list there are a dulicate value but remove always firsst value)
fruits=["Apple","Mangoo","Grap","Orrange","Banana","Apple"]
fruits.remove("Apple")
print(fruits)


fruits=["Apple","Mangoo","Grap","Orrange","Banana"]
fruits.pop(0)
print(fruits)


fruits=["Apple","Mangoo","Grap","Orrange","Banana"]
del fruits[1]
print(fruits)

fruits=["Apple","Mangoo","Grap","Orrange","Banana"]
fruits.clear()
print(fruits)