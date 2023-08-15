'''
Exception Handling:

Types of errors:
1. Syntax errors- these are not exceptions. Programmer is completely responsible for this
2. Runtime errors
'''


# a=3
#
# if a>0
#     print(a)

a= 8
b= 2
print(a+b)
print(a-b)
print(a*b)
print(a*0)
print(a/b)
# print(a/"zero")
try: 
    try:
        print(a/4)
    except ZeroDivisionError as ze:
        print(ze)
except TypeError as te:
    print(te, ": error in 'a/zero'")
finally:
    print("program exceuted successfully")
# print(a%b)
# print(a//b)