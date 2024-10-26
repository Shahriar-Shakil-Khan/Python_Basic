'''
def y (Email,Reference):
    x=Email+" "+Reference
    print(x)
    
y("shshriarshakil28@gmail.com","Shahriar Shakil")    
'''
'''
def y (Email,Reference):
    x=Email+"   "+Reference
    print(x)
    
y("shshriarshakil28@gmail.com")        # 1 perameter so it's wrong and it will show error
 

def function(*details):
    print(details)
    
function(101,"Nabil",3.75,"Akua","College")   


def function(*kids):
    print(kids)
    
function(102,"Shakil",3.74,"Dhaka","uNIVERSITY",780,"GG")   

def function(*kids):
    print(kids[5])
    
function(102,"Shakil",3.74,"Dhaka","uNIVERSITY",780,"GG")   

def show():
    print("No Perameter")
    
show() 


def function(**k):
    print(k)
    
function(road=102,name="Shakil",cg=3.74,place="Dhaka",versity="AIUB")



def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def function(**k):
    
    for x,y in k.items():
        print(x," = ",y)
    
function(road=102,name="Shakil",cg=3.74,place="Dhaka",versity="AIUB")



def default(a,b=4):
    print("sum = ",a+b)
    
default(4,10)   #default value
 
def _list(_name):
     pass
     for name1 in _name:
      print(name1)
 
name=['shakil','Nabil','Sami','Mona']
_list(name)    
'''

