#Parent class/super/

class Animal:

    def speak(self):
        print('Animal is speaking')

#child class/sub class/derived class
class Dog(Animal):
    def bark(self):
        print('Dog is barking')


class Cat(Dog):
    def meow(self):
        print('Cat is meowing')


a = Animal()

d = Dog()

c = Cat()

