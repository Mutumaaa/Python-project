# Built-In Functions?Standard-Library function

y = max(45, 89, 75, 79, 56, 43)
print("The maximum value is", y)

x = min(45, 89, 75, 79, 56, 43,)
print("The minimum value is", x)

# User-defined functions
def school():
    print("Emobilis")

school()

def add():
    num1 = 5
    num2 = 10
    print(num1 + num2)

add()

#parameter/variable and argument/value
def multiply(a, b):

    print(a * b)
multiply(5,6)
multiply(10,3)

def employee(name, age, gender, salary, position):
   print(name, age, gender, salary, position)

employee("Sharrif",24,"Male",5600000,"CEO")
employee("Lorna",24,"Female",5600000,"Director")
employee("Peace",24,"Female",5600000,"Doc")
employee("Daniel",24,"Male",5600000, "Business manager")
employee("Jessica",24,"Male",5600000,"Surveyor")



#A program to display details of 5 patients
#Using a user defined function, implement parameter
#and argument
#full name, gende, age, disease

def patient(fullname, gender, age, disease):
    print(fullname, gender, age, disease)


patient("Patric", "male", 55, "Typhoid")
patient("Mavin", "male", 35, "livermorium")
patient("Ruro", "male", 55, "Tuberculosis")
patient("kimmicc", "male", 55, "Tuberculosis")
patient("Patric", "male", 55, "Cancer")



