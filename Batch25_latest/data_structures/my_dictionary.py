a={}
print(type(a))
print("a -->", a)

b={1:"Anjusha", 2:"Kruthi", 3:"Mohith"}
print(type(b))
print("b -->", b)

c=dict()
print(type(c))
print("c -->", c)

d=dict([(4,"Praveen"), (5, "Preetha"), (6,"Vivek")])
print("d -->", d)

b[4]="Praveen"
print("b -->", b)

b[3]="Preetha"
print("b -->", b)

b[5]="Kruthi"
print("b -->", b)

print(b[3])

# b.clear()
# print("b -->", b)

e=b.fromkeys((1, 2, 3, 4), "Name")
print("b -->", b)
print("e -->", e)

f=b.items()
print(f)

g=b.keys()
print(g)

h=b.popitem()
print(h)

b.setdefault(6)
print("b -->", b)

k=b.values()
print(k)



