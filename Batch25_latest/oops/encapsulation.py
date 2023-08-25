'''
Encapsulation:

Capsule?

_ --> protected variable
__ --> private variable
'''


class Operation:
    def __init__(self, r):
        self.r=r
        self.__pi=3.142
        
    def circumference(self):
        c=2*self.__pi*self.r
        print(c)
        
circle1=Operation(5)
circle1.circumference()
# print(circle1.r)
# print(circle1._pi)
# circle1._pi=4.5
# print(circle1._pi)
# circle1.circumference()
# print(circle1.__pi)
print(dir(circle1))
print(circle1._Operation__pi) # name mangling