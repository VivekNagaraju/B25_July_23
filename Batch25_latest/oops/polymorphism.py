'''
Polymorphism:

Poly= many
Morph= forms

'+' --> addition, list extend and string concatenation (Operator Overloading)
'*' -->

Types:

1. Over-riding: One method/ constructor is overriding the another method with the same name
    a. Method Over-riding
    b. Constructor Over-riding
2. Overloading:same operator/method/constructor used for multiple purposes 
    a. Operator Overloading 
    b. Method Overloading
    c. Constructor Overloading
'''

class Operations:
    def sum(self, a, b):
        print(a+b)
        
        
opt1=Operations()
opt1.sum(2, 4, 3)

