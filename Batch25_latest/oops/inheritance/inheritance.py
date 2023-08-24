from abc import *

class GrandFather(ABC):
    def gf_f(self):
        print("This is GF function")
     
    @abstractmethod   
    def govt_job(self):
        pass

class Father(GrandFather):
    def f_f(self):
        print("This is Father function")
        
    # def govt_job(self):
    #     print("This is Dad's job")
    
class Mother():
    def mother_fun(self):
        print("This is Mother Function")  
        
    def govt_job(self):
        print("This is Mom's job")
              
class MyClass(Father, Mother):
    def my_function(self):
        print("This is My function")
        
    def govt_job(self):
        print("This is my job")
        
# ajja=GrandFather()
# ajja.gf_f()
# print(GrandFather.__dict__)

# appa=Father()
# appa.f_f()
# print(Father.__dict__)
# appa.gf_f()

nanu=MyClass()
nanu.gf_f()
nanu.f_f()
nanu.my_function()
nanu.mother_fun()
nanu.govt_job()

print(MyClass.mro())

'''
MRO- Method Resolution Order
MyClass(Father, Mother): MyClass-->Father-->GrandFather-->Mother
MyClass(Mother, Father): MyClass-->Mother--->Father-->GrandFather

'''