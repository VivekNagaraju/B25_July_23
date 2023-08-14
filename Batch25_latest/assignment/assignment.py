# n=int(input("enter an integer:"))
# factorial=1
# for x in range(1,n+1):
#     factorial=factorial*x
# print(factorial)
#

# fibanocci:
# 0,1,1,2,3,5,8,.... 


# a=0
# b=1
# sum=0
# print(a)
# print(b)
# for x in range(0,b+1):
#    sum=sum+x
#

   
# def total(*n):
#     return n 
#
# def praveen(n):
#     c=sum(n)
#     print(c)
#
# praveen(total(2,5,6,44,8))

# def vivekshetty(*n):
#     print(sum(n))
#
# vivekshetty(2,5,6,3,4)

def total(*n):
    plus=0
    print(type(n))
    for x in n:
        plus+=x 
    print(plus)
    
total(2,5,6,8)