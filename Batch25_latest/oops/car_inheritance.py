class Car():
    def no_of_wheels(self):
        print("No of wheels is 4")
        
    def move_forward(self):
        print("Car is moving forward")
        
    def move_backward(self):
        print("Car is moving backward")
        
class HatchBack(Car):
    def hatch_back_function(self):
        print("This is hatchBack function")
        
    def less_space(self):
        print("Hatchbacks have lesser space")   
        
class Sedan(Car):
    def sedan_function(self):
        print("This is sedan function")
        
class SUV(Car):
    def suv_function(self):
        print("This is SUV Function")
        
    def drive_off_road(self):
        print("We can go off road with SUVs")  
         
    def higher_loads(self):
        print("SUV Carries Hhigher loads")
        
        
maruti_swift=HatchBack()
maruti_swift.hatch_back_function()
maruti_swift.move_forward()

honda_city=Sedan()
honda_city.sedan_function()
honda_city.move_forward()


duster=SUV()
duster.drive_off_road()
duster.move_forward()