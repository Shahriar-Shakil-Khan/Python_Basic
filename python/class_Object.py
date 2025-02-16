'''
class student():
    
    Id=""
    Cgpa=""

rahim=student()
rahim.Id=101
rahim.Cgpa=3.75
print(f"ID = {rahim.Id} , Cgpa = {rahim.Cgpa}")   

rahik=student()
rahik.Id=102
rahik.Cgpa=3.70
print(f"ID = {rahik.Id} , Cgpa = {rahik.Cgpa}")   

rahima=student()
rahima.Id=103
rahima.Cgpa=3.0
print(f"ID = {rahima.Id} , Cgpa = {rahima.Cgpa}")   

'''

'''
class student():
    
    Id=""
    Cgpa=""
    
    def display(self):
     print(f"ID = {self.Id} , Cgpa = {self.Cgpa}")  



rahim=student()
rahim.Id=101
rahim.Cgpa=3.75
rahim.display()
#print(f"ID = {rahim.Id} , Cgpa = {rahim.Cgpa}")   

rahik=student()
rahik.Id=102
rahik.Cgpa=3.70
rahik.display()
#print(f"ID = {rahik.Id} , Cgpa = {rahik.Cgpa}")   

rahima=student()
rahima.Id=103
rahima.Cgpa=3.0
rahima.display()
#print(f"ID = {rahima.Id} , Cgpa = {rahima.Cgpa}") 

'''
'''
class student():
    
    Id=""
    Cgpa=""
    
    def set_value(self,Id,Cgpa):
       self.Id=Id
       self.Cgpa=Cgpa
        
    def display(self):
      print(f"ID = {self.Id} , Cgpa = {self.Cgpa}")  



rahim=student()
rahim.set_value(101,3.78)
rahim.display()


rahik=student()
rahik.set_value(102,3.8)
rahik.display()


rahima=student()
rahima.set_value(103,3.98)
rahima.display()
'''

class student():
    
    Id=""
    Cgpa=""
    
    def __init__(self,Id,Cgpa):
       self.Id=Id
       self.Cgpa=Cgpa
        
    def display(self):
      print(f"ID = {self.Id} , Cgpa = {self.Cgpa}")  



rahim=student(101,3.78)
rahim.display()

rahik=student(102,3.8)
rahik.display()

rahima=student(103,3.98)
rahima.display()