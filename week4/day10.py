'''
Concepts Of OOP (continued):
- Encapsulation
-polymorphism

Polymorphism 
Polymorphism means one action, many forms.

Real-life example:
When you click Play on:
YouTube → it plays a video
Spotify → it plays music
A game → it plays animations

Encapsulation is about protecting data inside a class.
It means keeping data (properties) and methods together 
in a class, while controlling how the data can be accessed from outside the class.

Why Use Encapsulation?
Data Protection: Prevents accidental modification of data
Validation: You can validate data before setting it
Flexibility: Internal implementation can change without affecting external code
Control: You have full control over how data is accessed and modified

'''
# polymorphism

class Dog:
    def noise(self):
        return 'barks'

class Snake:
    def noise(self):
        return 'hiss'

class Cat:
    def noise(self):
        return 'meow'

my_dog = Dog()
my_snake = Snake()
my_cat = Cat()

# print(my_dog.noise())
# print(my_snake.noise())
# print(my_cat.noise())


# polymorphim example 2
class Car:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Drive!")

class Boat:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Sail!")

class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly!")

car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object

for x in (car1, boat1, plane1):
  x.move()


# encapsulation
class Data:
    def __init__(self, name, age):
        self.name = name
        self.__age = age  # this has made the age to become private

    def get_age(self):
        return self.__age

nelson = Data('nelson', 36)
print(nelson.name )
print(nelson.get_age())


# encapsulation 2
class Biodata:
    def __init__(self,name,level,cgpa,address):
        self.name = name
        self.level = level
        self.__cgpa = cgpa
        self.__address = address

    # we write a function to get the private(encapsulated data)
    def get_cgpa(self):
        return self.__cgpa

    def get_address(self):
        return self.__address

bio_form = Biodata('nelson',400,4.9,'MAu')
print(bio_form.name)
print(bio_form.level)
print(bio_form.get_cgpa())
print(bio_form.get_address())
