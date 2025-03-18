class trianagle():
    
    base=""
    height=""
    
    def __init__(self, base, height):
        
        self.base=base
        self.height=height
    
    def display(self):
        
        area =0.5*self.base*self.height
         
        print(f"The area of triangle is : = {area}")    
        
base = float(input("Enter the base of the triangle: "))
height = float(input("Enter the height of the triangle: "))       

Trangle=trianagle(base,height) 
Trangle.display()       