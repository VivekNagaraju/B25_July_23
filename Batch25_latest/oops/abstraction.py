'''
Abstraction: Concepts in Idea but not implemented

Types of methods:
1. Implemented methods/ concrete methods
2. Un-implemented methods
3. Abstract methods

Abstract class contains both implemented and abstract methods
Interfaces contains only abstract methods
'''
from abc import *

class Car(ABC):
    def no_of_wheels(self):
        print("No of wheels is 4")
        
    def move_forward(self):
        print("Car is moving forward")
        
    def move_backward(self):
        print("Car is moving backward")
    
    @abstractmethod  
    def length_of_car(self):
        pass
        
class HatchBack(Car):
    def hatch_back_function(self):
        print("This is hatchBack function")
        
    def less_space(self):
        print("Hatchbacks have lesser space")   
     
    def length_of_car(self):
        print("Length of the car is 3800mm") 
        
class Sedan(Car):
    def sedan_function(self):
        print("This is sedan function")
        
    def length_of_car(self):
        print("Length of the car is 4500mm")
        
class SUV(Car):
    def suv_function(self):
        print("This is SUV Function")
        
    def drive_off_road(self):
        print("We can go off road with SUVs")  
         
    def higher_loads(self):
        print("SUV Carries Hhigher loads")
        
    def length_of_car(self):
        print("Length of the car is 6000mm")
        
        
maruti_swift=HatchBack()
maruti_swift.hatch_back_function()
maruti_swift.move_forward()
maruti_swift.length_of_car()

honda_city=Sedan()
honda_city.sedan_function()
honda_city.move_forward()
honda_city.length_of_car()

duster=SUV()
duster.drive_off_road()
duster.move_forward()
duster.length_of_car()