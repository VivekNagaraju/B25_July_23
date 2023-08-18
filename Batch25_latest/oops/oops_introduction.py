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

vinayak=Student("Vinayak") #creating an object
print(dir(vinayak))
print(Student.__dict__)
vinayak.write_code(101)
vinayak.display_details()
# vinayak=Student("Vinayak2", 2)
# vinayak.write_code

# print(type(vinayak))

chetan=Student("Chethan")
chetan.write_code(201)
chetan.display_details()
# vinayak.write_code()
# chetan.write_code()
# print(vinayak.name)
# print(chetan.name)
# print(type(chetan))
