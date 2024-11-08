name_demo=" Shahriar Shakil "
print(name_demo)

print()

name1="Shahriar "
name2="Shakil"

x=name1+name2
print(x)

name1="Zakaria"
name2="Nabil"

x=name1+" "+name2
print(x)

name3="Masud"
name4="Rana"
name5="Shagor"                       # here join method

name4=" ".join([name3,name4,name5])
print(name4)

name6="Masum"
name7="khan"                        #%format method
name8="%s %s"%(name6,name7)
print(name8)


name9="Masum"
name10="khan"                        #%format method
name11="{}:{}".format(name9,name10)
print(name11)




