'''

'''
#creating a class
class Student:
    college="iQuest" # class/  static  variables
    def __init__(self, name):
        self.name=name #instance/ object variables
        # self.roll_no=roll_no
        # Student.college="iQuest" # declaring static variable inside the constructor
        print(f"This is {self.name} constructor")
    
    
    def write_code(self, roll_no): 
        # roll_no=roll_no #method variables
        self.roll_no=roll_no # instance variable inside a method
        print(f"{self.name} writing the code")
    
       
    def display_details(self):
        # Student.college="iQuest"
        print(f"Name of the student is {self.name}, ID is {self.roll_no} and college name is {Student.college}")

std1=Student("Vinayak") #creating an object
print(dir(std1))
print(Student.__dict__)
std1.write_code(101)
std1.display_details()
# vinayak=Student("Vinayak2", 2)
# vinayak.write_code

# print(type(vinayak))

std2=Student("Chethan")
std2.write_code(201)
std2.display_details()
# vinayak.write_code()
# chetan.write_code()
# print(vinayak.name)
# print(chetan.name)
# print(type(chetan))
