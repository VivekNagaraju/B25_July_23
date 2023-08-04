# a=1
# b=2
# print(a+b)

name = 'Prem Raj'
print("Name of the employee is:", name)

address = """ Infosys,
Electronics City,
Bengaluru.
"""

print("Address of the employee is:",address)

welcome_txt= 'Welcome to "Python" classes'
print(welcome_txt)

print(name[2])
print(name[-2])
print(name[0 : 4])
print(name[ : 4])
print(name[1 : 4])
print(name[0 : 8 : 2])
print(name[ : : -1])

print("===============check pallindrome============")
place1="mysuru"
place2=place1[ : : -1]
print("place1 -->", place1)
print("place2 -->", place2)
print(place1 == place2)

print("==============mutability===============")
# name[2]="a"
print(name) #string is immutable

print("===============OPerators================")
a="Vinayak"
b="vivek"
c="Vivek"

print(a+b) # string concatination without space
print(a,b) # string concatination with space

print(a*2)

print("a" not in b)

print(b == c)

print("===========pre-defined functions==========")
d=c.casefold()
print("d-->", d)

print(d.count("v"))

# d.index("k", 0, 4)
print(d.index("v", 0, 5))

e= "   anjusha  "
print(e+"abc")
print(e.lstrip()+"abc")

print(d.rfind("v", 0, 5))

f=["kruthi", "mohith", "preetha"]
g="".join(f)
print(g)



