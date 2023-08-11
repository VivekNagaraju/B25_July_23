def sum(a, b): # formal arguments. (Arguments are variables used to send input to the functions)
    c=a+b
    print(c)
    
# sum(2, 3) # actual arguments

def find_energy(m, c=6): # default arguments
    e=m*c**2
    print(e)
    
# find_energy(2)
# find_energy(3)

def add(*a): # variable length arguments
    print(a)
    
# add(1, 2, 3 , 4, 5, 6 )

def display(**a): # keyword variable length arguments
    print(a)
    
# display(a1=2, b2=4, name="Vivek", object="pen", decimal=3.5)

