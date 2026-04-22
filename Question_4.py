class Student:
    def __init__(self, name, roll_number):
        self.name = name
        self.roll_number = roll_number
        self.age = 0
        self.marks = 0

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

    def Display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll_number)
        print("Age:", self.age)
        print("Marks:", self.marks)

student1 = Student("Alice", 101)
student1.setAge(20)
student1.setMarks(85)
student1.Display()