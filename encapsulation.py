#simple program to demonstrate encapsulation

class Person:
    def __init__(self, name, age):
        self.name = name  # Public attribute
        self.__age = age  # Private attribute

    def get_age(self):  # Getter method
        return self.__age

    def set_age(self, age):  # Setter method
        if age > 0:
            self.__age = age

# Creating an object
p = Person("Alice", 25)

print(p.name)  # Accessing public attribute
print(p.get_age())  # Accessing private attribute using getter

p.set_age(30)  # Modifying private attribute using setter
print(p.get_age())
