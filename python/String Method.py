
#uppercase
name1="shakil"
x=name1.upper()
print(x)

#Lowercase
name2="SHAKIL"
y=name2.lower()
print(y)

name3="masum"
z=name3.capitalize()
print(z)


name4="masud rana"
z1=name4.title()
print(z1)

name5="bristy Akter"
z2=name5.swapcase()
print(z2)


name6='Shahriar khan'
c=name6.replace('khan','Shakil' )
print(c)


name7='1/2//3/4/5'
c1=name7.split("/")
print(c1)

num=['1', '2', '', '3', '4', '5']
c3="".join(num)
print(c3)

name7='  shakil  '
name8=name7.strip()
print(name8)

name7='  shakil  '
name8=name7.lstrip()
print(name8)

name7='  shakil  '
name8=name7.rstrip()
print(name8)


text = 'Hello Shakil'
print(text.startswith('Hello'))
print(text.startswith('Shakil'))
print(text.endswith('Hello'))
print(text.endswith('Shakil'))
print(text.find("kil"))      # position
print(text.count("l"))       #count

text = 'Hello Shakil'
print(text.isalnum())
print(text.isalpha())
print(text.isdigit())

x='  '
print(x.isspace())

y1='Zakaria Nabil'
print(y1.istitle())


v=" i am shahriar shakil.i am from Mymensingh "
print(v.title().strip().upper())

