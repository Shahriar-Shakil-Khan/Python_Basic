'''
s=["c++","c","toc","compiler","java"]

print(s)
print(s[2])
print(s[2 :])
print(s[-4])
print("c" not in s)
print(s*2)
print(len(s))

s.append("OPP1")
print(s)
s.insert(3,"OS")
print(s)
s.remove("java")
print(s)
s.sort()
print(s)

s.reverse()
print(s)

s.pop()
print(s)
s1=s.copy()
print(s1)
position=s.index("c")
print(position)
item=[2,3,4,2,5,2,9]
it=item.count(2)
print(it)

x=list(("Apple","Banana","Orrange","Graps"))
print(x)
print(s)



t = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
      #0        #1        #2        #3       #4      #5        #6        

print(t[3:6])



t = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
      #0        #1        #2        #3       #4      #5        #6        

print(t[:3])


t = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
      #0        #1        #2        #3       #4      #5        #6     
      
if "Banana" in t:
    print("yes")
else:
    print("no")
    

t = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
      #0        #1        #2        #3       #4      #5        #6   

t[1]="grap"
print(t)

print(t[-3:-2])

'''

x=["A","B","C"]
y=["D","E","F"]
x.extend(y)
print(x)