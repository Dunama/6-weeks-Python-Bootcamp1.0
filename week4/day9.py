'''
Object Oriented Programming (OOP)
Python is an object-oriented language, allowing you to 
structure your code using classes and objects for better organization and reusability

Advantages of OOP
.Provides a clear structure to programs
.Makes code easier to maintain, reuse, and debug
.Helps keep your code DRY (Don't Repeat Yourself)
.Allows you to build reusable applications with less code

Concepts Of OOP:
-CLASS
-OBJECTS
A class defines what an object should look like, and an object is created based on that class. For example:
Class	Objects
Fruit	Apple, Banana, Mango
Car	Volvo, Audi, Toyota

'''
class Fruits:
    def __init__(self, name):
        self.name = name
        
gift = Fruits('watermelon')
gift.name

class Cars:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Cars('Lexus', 2023)
car2 = Cars('BMW', 2025)
car3 = Cars('Dodge', 2001)

print(car1.brand, car1.model)
print(car2.brand, car2.model)
print(car3.brand, car3.model)


class School:
    def __init__(self, name, level, dept):
        self.name = name
        self.level = level
        self.dept = dept

name = input('name: ')
level = input('level: ')
dept = input('department: ')

print(name)
print(level)
print(dept)