class Employee:
    def __init__(self, Name, position, salary):
        self.Name = Name
        self.position = position
        self.salary = salary

    def info(self):
        print(self.position, "is earning", self.salary)

employee1 = Employee("John", "CEO", 20000)
print(employee1.Name, employee1.position, employee1.salary)
employee1.info()

employee2 = Employee("John", "Human resource", 20000)
print(employee2.Name, employee2.position, employee2.salary)
employee2.info()
employee3 = Employee("John", "Human resource", 20000)
employee4 = Employee("John", "Human resource", 20000)
employee5 = Employee("John", "Human resource", 20000)


