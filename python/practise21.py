'''
with open("example.com","w") as file:
    #file.write("Hello World!")
    file.write("Hello Shakil!")
    #print("created")

with open("example.com","r") as file:
    content=file.read()
    print(content)



import os
os.rename("example.com","new_example.text")



import os
os.remove("new_example.text")

'''

import os
os.remove("new/r.text")