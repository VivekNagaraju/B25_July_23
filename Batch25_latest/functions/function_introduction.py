'''
a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=a+b
print(c)

a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=a+b
print(c)

a=int(input("Enter a number"))
b=int(input("Enter another number"))
c=a+b
print(c)
'''

def welcome_message(): # function without arguments/ parameters
    print("Welcome to iQuest")
    
def sum(a, b): # fuction with arguments/ parameters
    c=a+b
    # print(f"Sum of {a} and {b} is",c)
    return c
    
def multiplication(a, b): # fuction with arguments
    c=a*b
    # print(f"Multiplication of {a} and {b} is",c)
    return c

def double(a):
    print(f"double of {a} is", a*2)    
welcome_message()
# d=sum(6,2) #positional arguments
# print(d)
# print(d*2)
double(sum(6, 2)) # passing function as argument to another function
sum(5, 5)
sum(b=4, a=6) #keyword arguments
sum(7, 8)

print(multiplication(5, 8)) # passing user defined function as argument for pre-defined/ built-in function
double(multiplication(5, 8)) # passing user defined function as argument for another user-defined function