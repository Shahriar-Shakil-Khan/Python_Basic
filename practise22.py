
import os

os.mkdir("new")


import os

#os.mkdir("new1")

dirItem=os.listdir(".")
print(dirItem)

with open("new1/r.text","w") as file:
    file.write("Hello world!")



import os

#os.rename("new","new_new")
#os.remove("new_new/t.text")
os.rmdir("new_new")



import os

filelist=os.listdir("new1")
#print(filelist)
for x in filelist:
    print(x)



















