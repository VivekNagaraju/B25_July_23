# a=int(input("enter the starting range:"))
# b=int(input("enter the stoping range"))
# for num in range(a, b):
#     if num %2==1:
#         print(num)
b=int(input("enter an integer"))
# even=[]
# for x in range(1,b):
#     if x%2==0:
#         even.append(x)
even=[x for x in range(1, b) if x%2==0] # list comprehension
print(even)
       
# number=[8,16,19,360,720,750,49,19,819]  
# even= []
# odd=  []    
# for i in number:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)     
# print("even ",even) 
# print("odd",odd)       
        
        
        
