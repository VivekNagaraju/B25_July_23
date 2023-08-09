def sum(a, b): # fuction with arguments/ parameters
    sum=a+b
    return sum
    
def multiplication(a, b): # fuction with arguments
    mul=a*b
    return mul

def sum_mul(a, b):
    s=sum(a, b) # calling one function inside another function
    m=multiplication(a, b)
    return s, m # returning multiple values 

c=sum(2, 3)
d=multiplication(2, 3)
e, f=sum_mul(2, 3) #  storing multiple return values in 2 different variables

print(c)
print(d)
print(e)
print(f)

'''
Assignments:
1. Factorials: Take an interger as user input, 
call the factorial function with user input as argument and print the output
Ex: 3!=3*2*1=6; 5!=5*4*3*2*1=120

2. Fibnocci series: 0, 1, 1, 2, 3, 5, 8, 13.....

Take an integer as user input, 
call fibnocci function with user input as argument and print the fibnocci series

Hint: calling function within function

3. sum all the elements present in the tuple
'''




