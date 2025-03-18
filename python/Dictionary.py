'''
student={
    
    "101" : "Shakil",
    "102" : "Mahadi",
    "103" : "Rafi"
    
}

print(student.get("103","Not a Valid key"))

student={
    
    101 : "Shakil",
    102 : "Mahadi",
    103 : "Rafi"
    
}

x=student[101]
y=student.get(102,"Not A valid key")
print(x)
print(y)



student={
    
    101 : "Shakil",
    102 : "Mahadi",
    103 : "Rafi"
    
}

#student.update({103:"Nabil"})
#student.pop(102)
#del student[103]
#student.clear()

for x in student:
    
 print(student[x])

students={
    
    501 : "nobel",
    502 : "Simu",
    503 : "Sami"
    
}
for x, y in students.items():
    print(x," : ", y)
    


 
students={
    
    501 : "nobel",
    502 : "Simu",
    503 : "Sami"
    
}
for x in students.keys():
    print(x)

for x in students.values():
    print(x)    

 
 
 
student={
     "1" : "Shakil",
     "2" : "Nabil",
      "3" : "Simu",
     "4" : "Sami"
}

#student_file=student.copy()
student_file=dict(student)
print(student_file)




# Here it nested dictionary

child={
    
    "child1" :{
        101 :"loin",
        102 :"Elephant",
        103 :"Tiger"
    },
    "child2" :{
        104 :"Apple",
        105 :"orrange",
        106 :"Banana"
    },
    "child3" :{
        107 :"Onion",
        108 :"Ladis_Finger",
        109 :"Tamoto"
    }
}

print(child)  


# Another Way nested loop
child1={
        101 :"loin",
        102 :"Elephant",
        103 :"Tiger"
    }
child2 ={
        104 :"Apple",
        105 :"orrange",
        106 :"Banana"
    }
child3 ={
        107 :"Onion",
        108 :"Ladis_Finger",
        109 :"Tamoto"
    }
    
family={
    "child1": child1,
    "child2": child2,
    "child3": child3,
} 

print(family)   

'''