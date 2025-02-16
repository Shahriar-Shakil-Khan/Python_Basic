#Rectangle Area
print("------------Rectangle Area-----------")
w=float(input("Enter width  : "))
h=float(input("Enter height : "))

area=w*h
print("The answer of Rectangle area is ",area)
print("/n")


#Triangle Area
print("------------Triangle Area-----------")
b=float(input("Enter base  : "))
h=float(input("Enter vertical height : "))

area=0.5*w*h
print("The answer of Triangle area is ",area)
print("/n")

#Trapezoid Area
print("------------Trapezoid Area-----------")
a=float(input("Enter upper base  : "))
b=float(input("Enter lower base  : "))
h=float(input("Enter vertical height : "))

area=0.5*(a+b)*h
print("The answer of Trapezoid area is ",area)
print("/n")



#Square Area
print("------------Square Area-----------")
length=float(input("Enter length  : "))


area=length*length
print("The answer of Square area is ",area)
print("/n")

#Circle Area
#from math import*
import math
print("------------Circle Area-----------")
r=float(input("Enter  radius  : "))


area= math.pi * r**2
print("The answer of radius area is ",area)
print("/n")