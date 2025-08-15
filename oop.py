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
# The __str__() method controls what should be returned when the class
#  object is represented as a string.

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


# Add the __init__() function to the Student class:

     
# class Student(Person):
  # def __init__(self, fname, lname):
  
# When you add the __init__() function, the child class will no 
# longer inherit the parent's __init__() function.
# Note: The child's __init__() function overrides the inheritance
#  of the parent's __init__() function.


# To keep the inheritance of the parent's __init__() 
# function, add a call to the parent's __init__() function:

class Student(Person):
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname)

# Now we have successfully added the __init__() function, 
# and kept the inheritance of the parent class, and we are
#  ready to add functionality in the __init__() function.


# Use the super() Function
# Python also has a super() function that will make the child class inherit
#  all the methods and properties from its parent:

class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
# By using the super() function, you do not have to use the name of the
#  parent element, it will automatically inherit the methods and properties from its parent.

class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)
# Add a property called graduationyear to the Student class:
  # In the example below, the year 2019 should be a variable, and passed into the Student class when creating student objects. To do so, add another 
  # parameter in the __init__() function:
  # Add a year parameter, and pass the correct year when creating objects:
class Student(Person):
  def __init__(self, fname, lname, year):
    super().__init__(fname, lname)
    self.graduationyear = year

x = Student("Mike", "Olsen", 2019)
print(x.graduationyear)
print(x)


# Python Iterators
# An iterator is an object that contains a countable number of values.

# An iterator is an object that can be iterated upon, meaning that 
# you can traverse through all the values.

# Technically, in Python, an iterator is an object which implements 
# the iterator protocol, which consist of the methods __iter__() and __next__().

# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. 
# They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))


# Even strings are iterable objects, and can return an iterator:
myStr = "Fuck You"
iterableStr=iter(myStr)
print(next(iterableStr))
print(next(iterableStr))
print(next(iterableStr))

# Create an iterator that returns numbers, starting with 1, and each 
# sequence will increase by one (returning 1,2,3,4,5 etc.):

class MyNumbers:
  def __iter__(self):
    self.num=1
    return self
  def __next__(self):
    outputNum=self.num
    self.num +=1
    return outputNum

myClass = MyNumbers()
myIter=iter(myClass)

print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))


# StopIteration
# The example above would continue forever if you had enough 
# next() statements, or if it was used in a for loop.

# To prevent the iteration from going on forever, 
# we can use the StopIteration statement.

# In the __next__() method, we can add a terminating condition to 
# raise an error if the iteration is done a specified number of times:

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      self.a += 1
      x = self.a
      return x
    else:
      raise StopIteration

myclass=MyNumbers()
myIter = iter(myclass)

# for x in myIter:
  # print(x)


# The word "polymorphism" means "many forms", and in programming
#  it refers to methods/functions/operators with the 
# same name that can be executed on many objects or classes.

# An example of a Python function that can be used on different objects is the len() function.

# String
# For strings len() returns the number of characters:

# ExampleGet your own Python Server
y = "Hello World!"
print(len(y))

# For tuples len() returns the number of items in the tuple:

# Example

mytuple = ("apple", "banana", "cherry")

print(len(mytuple))

# For dictionaries len() returns the number of key/value pairs in the dictionary:

# Example

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(len(thisdict))



# Different classes with the same method:
class Car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("Drive Car!")

class Boat:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def move(self):
    print("Sail Boat!")


class Plane:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Fly Plane!")


neCar=Car("Ford","Mustang")
neBoat=Boat("Ibiza","Touring 20")
nePlane=Plane("Boeing","747")

for i in (neCar,neBoat,nePlane):
  i.move()


# Inheritance Class Polymorphism
# What about classes with child classes with the same name? Can we use polymorphism there?

# Yes. If we use the example above and make a parent class called Vehicle, 
# and make Car, Boat, Plane child classes of Vehicle, the child classes inherits 
# the Vehicle methods, but can override them:

# Example
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(Vehicle):
  pass

class Boat(Vehicle):
  def move(self):
    print("Sail")

class Plane(Vehicle):
  def move(self):
    print("Fly")


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object


for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()