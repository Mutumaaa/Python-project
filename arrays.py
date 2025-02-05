courses = ["MIT", "Cyber security", "Data science", "Data engineering"]
print(courses)


# Accessing an element
print(courses[2])

#Looping through an array
for x in courses:
    print("Course is",x)

# Adding a new element into an array
courses.append("Laravel")
print(courses)

# Removing an element
courses.remove("Cyber security")
print(courses)
