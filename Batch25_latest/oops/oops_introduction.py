'''

'''
#creating a class
class Student:
    college="iQuest" # class/  static  variables
    def __init__(self, name, roll_no):
        self.name=name #instance/ object variables
        self.roll_no=roll_no
        print(f"This is {self.name} constructor")
        
    def write_code(self): #method variables
        print(f"{self.name} writing the code")
        
    def display_details(self):
        print(f"Name of the student is {self.name} and ID is {self.roll_no}")

vinayak=Student("Vinayak", 1) #creating an object
# vinayak.write_code()
# vinayak.display_details()
# vinayak=Student("Vinayak2", 2)
# vinayak.write_code

# print(type(vinayak))

chetan=Student("Chethan", 2)
# chetan.write_code()
# vinayak.write_code()
# chetan.write_code()
# print(vinayak.name)
# print(chetan.name)
# print(type(chetan))
