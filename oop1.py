class Student:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age


def study(self):
    print(self.name, "is studying")

student1 = Student("Breanna", "Female", 18)
student2 = Student("Daniella", "Male", 18)
student3 = Student("Lorna", "Female", 18)
student4 = Student("Jessica", "Male", 18)
student5 = Student("Fiona", "Female", 18)

print(student1.name, student1.gender, student1.age)
