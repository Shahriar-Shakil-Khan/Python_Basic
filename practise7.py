
x=['A','B','C','D','A','E']
for list1 in x:
    print(list1)


x=['A','B','C','D','A','E']

for i in range(len(x)):
    print(x[i])



x=['A','B','C','D','A','E']
i=0
while i<len(x):
    print(x[i])
    i=i+1

x = ['A', 'B', 'C', 'D', 'A', 'E',
     'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
      'W', 'X', 'Y', 'Z']

i=0
while i<len(x):
    print(x[i])
    i=i+1


x = ['A', 'B', 'C', 'D', 'A', 'E',
     'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
      'W', 'X', 'Y', 'Z']

[print(list2) for list2 in x]