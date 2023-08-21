
class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age
        print("This is Person class constructor")
        
    def person_details(self):
        print(f"Name of the person is {self.name} and age is {self.age}")
        
    def walk(self):
        print(f"{self.name} is walking")

class Student(Person):
    def __init__(self, name, age, roll_no):
        super().__init__(name, age)
        self.roll_no=roll_no
        print("This is Student class constructor")
    
    def student_details(self):
        print(f"Name of the student is {self.name}, age is {self.age} and roll no is {self.roll_no}") 

std1=Student("Vinayak", 16, 101)
std1.person_details()
std1.student_details()

