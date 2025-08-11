# OOP stands for Object-Oriented Programming.

# Python is an object-oriented language, allowing you to structure
#  your code using classes and objects for better organization
#  and reusability.


# Advantages of OOP
# Provides a clear structure to programs
# Makes code easier to maintain, reuse, and debug
# Helps keep your code DRY (Don't Repeat Yourself)
# Allows you to build reusable applications with less code
# Tip: The DRY principle means you should avoid writing the 
# same code more than once.
#  Move repeated code into functions or classes and reuse it



# Classes and objects are the two core concepts in object-oriented programming.

# A class defines what an object should look like, and an object 
# is created based on that class. For example:

# Class	Objects
# Fruit	Apple, Banana, Mango
# Car	Volvo, Audi, Toyota
# When you create an object from a class, 
# it inherits all the variables and functions defined inside that class.

# To understand the meaning of classes 
# we have to understand the built-in __init__() method.
# All classes have a method called __init__(), which is always 
# executed when the class is being initiated.

# Use the __init__() method to assign values to object properties,
#  or other operations that are necessary to do when the object is being created:

# Example
# Create a class named Person, use the __init__() method to assign values
#  for name and age:

class Person:
    def __init__(self,name,age):
        self.name=name;
        self.age=age;


person1 = Person("John",45);
print(person1.name)
print(person1.age)

# The __init__() method is called automatically
#  every time the class is being used to create a new object.


# The __str__() Method
# The __str__() method controls what should be returned when the class object is represented as a string.

# If the __str__() method is not set, the string representation of the object is returned:

# Example
# The string representation of an object WITHOUT the __str__() method:


        
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1)


# The string representation of an object WITH the __str__() method:

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person("John", 36)

print(p1)

# You can create your own methods inside objects. Methods in 
# objects are functions that belong to the object.
class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age
   def myFunction(self):
      print("Hello my name is " + self.name)

person1=Person("Chris",27)
person1.myFunction()


# The self Parameter
# The self parameter is a reference to the current instance of the 
# class, and is used to access variables that belong to the class.

# It does not have to be named self, you can call it whatever you
#  like, but it has to be the first parameter of any function in the class:

# Use the words mysillyobject and abc instead of self:

class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(abc):
    print("Hello my name is " + abc.name)
    print("My age is  " + str(abc.age))

p1 = Person("John", 36)
p1.myfunc()

# modify properties on object
p1.age=40
p1.myfunc()


# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods 
# and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.

# Create a Parent Class
# Any class can be a parent class, so the syntax is the same as creating any other class:

class Person:
   def __init__(self,firstname,lastname):
      self.firstname=firstname
      self.lastname=lastname
   def printName(self):
      print("FirstName is  " + self.firstname, " And The lastName is " + self.lastname )


#Use the Person class to create an object, and then execute the printname method:
newPerson = Person("John", "Doe")
newPerson.printName()

# Use the Student class to create an object, and then execute the printname method:
class Student(Person):
   pass

inheritPerson=Student("Mike","Olsen")
inheritPerson.printName()