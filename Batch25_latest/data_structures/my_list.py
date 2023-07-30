# a=[]
# print("a -->", a)
#
b=[1.0, 2.1, 3.2, 4.3, 5.4]
print("b -->",b)

c=list(range(1, 10))
print("c -->", c)

d=32
print("d -->", d)
# d=list(range(-5))
# print("d -->", d)
#
# e=list(range(-10, 0, 2))
# print("e -->", e)
#
# f=["swetha", "kavitha", "anjusha"]
# print("f -->", f)
#
# g=[1, 3.4, "vivek"]
# print("g -->", g)
#
# print("fetching 3rd element from the left -->", c[2]) # positive indexing
# print("fetching 2nd element from the right -->", c[-2]) # negative indexing
#
# print("===============slicing=============")
# print(c[1:6])
# print(c[:6])
# print(c[:8:2])
# print(c[::2])
# print(c[::-1])
# print(c[:5:-1])
#
# print(type(c))

c.append(20)
print("after appending 20 to list c -->", c)

c.append(d)
print("c after appending d -->", c)

# c.append(b)
# print("c after appending b -->", c)
#
# print(len(c))
# print(c[11])
c.extend(b)
print(c)
print(len(c))

print(c[8])
c[8]=99
print(c)
print(len(c))

