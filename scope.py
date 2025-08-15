# A variable is only available from inside the region it is 
# created. This is called scope.

# Local Scop
# A variable created inside a function belongs to the local scope 
# of that function, and can only be used inside that function.

def myFunction():
    x=40
    print(x);
myFunction()

# Function Inside Function
# As explained in the example above, the variable x is not available 
# outside the function, but it is available for any function inside the function:

def myfunc():
    x=50
    def myInnerFunc():
        print(x)
    myInnerFunc();
myfunc();

# Global Scope
# A variable created in the main body of the Python code 
# is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
# Example
# A variable created outside of a function is global and can be used by anyone:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# If you operate with the same variable name inside and outside of a function,
#  Python will treat them as two separate variables, one available in the
#  global scope (outside the function) and one available in the local scope 
# (inside the function):

# Example
# The function will print the local x, and then the code will print the 
# global x:

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)


# If you need to create a global variable, but are stuck in the local scope, you can use the global keyword.

# The global keyword makes the variable global.

# Example
# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = 700

myfunc()

print(x)


# Also, use the global keyword if you want to make a change to a global
#  variable inside a function.

# Example
# To change the value of a global variable inside a function, refer to 
# the variable by using the global keyword:

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)

# Modules of python 

# Consider a module to be the same as a code library.

# A file containing a set of functions you want to include in your application.

# Create a Module
# To create a module just save the code you want in a file with the file extension .py:

# ExampleGet your own Python Server
# Save this code in a file named mymodule.py

def greeting(name):
  print("Hello, " + name)

# Import the module named mymodule, and call the greeting function:

# import mymodule

# mymodule.greeting("Jonathan")


# Save this code in the file mymodule.py

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

# import mymodule

# a = mymodule.person1["age"]
# print(a)


# A date in Python is not a data type of its own, but we can import a module 
# named datetime to work with dates as date objects.

# Import the datetime module and display the current date:

import datetime

x = datetime.datetime.now()
print(x)

# Date Output
# When we execute the code from the example above the result will be:

# 2025-08-16 01:06:17.605610
# The date contains year, month, day, hour, minute, second, and microsecond.

# The datetime module has many methods to return information about the date object.

# Here are a few examples, you will learn more about them later in this chapter:

# Example
# Return the year and name of weekday:

import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A"))

# Creating Date Objects
# To create a date, we can use the datetime() class (constructor) of the datetime module.

# The datetime() class requires three parameters to create a date: year, month, day.

# Example
# Create a date object:

import datetime

x = datetime.datetime(2020, 5, 17)

print(x)

# The strftime() Method
# The datetime object has a method for formatting date objects into readable strings.

# The method is called strftime(), and takes one parameter, format, to specify the format of the returned string:

# Example
# Display the name of the month:

import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B"))


# Python has a set of built-in math functions, including an extensive math module, that allows you to perform mathematical tasks on numbers.

# Built-in Math Functions
# The min() and max() functions can be used to find the lowest or highest value in an iterable:

# ExampleGet your own Python Server
x = min(5, 10, 25)
y = max(5, 10, 25)

print(x)
print(y)


# The abs() function returns the absolute (positive) value of the specified number:

x = abs(-7.25)

print(x)


# The pow(x, y) function returns the value of x to the power of y (xy).

# Example
# Return the value of 4 to the power of 3 (same as 4 * 4 * 4):

x = pow(4, 3)

print(x)


# The Math Module
# Python has also a built-in module called math, which extends the list of mathematical functions.

# To use it, you must import the math module:

# import math
# When you have imported the math module, you can start using methods and constants of the module.

# The math.sqrt() method for example, returns the square root of a number:

import math

x = math.sqrt(64)

print(x)
# The math.ceil() method rounds a number upwards to its nearest integer, 
# and the math.floor() method rounds a number downwards to its nearest 
# integer, and returns the result:

import math

x = math.ceil(1.4)
y = math.floor(1.4)

print(x) # returns 2
print(y) # returns 1
# The math.pi constant, returns the value of PI (3.14...):

import math

x = math.pi

print(x)


# If you have a JSON string, you can parse it by using the json.loads() method.

# The result will be a Python dictionary.

# Example
# Convert from JSON to Python:

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])


# If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.

# Convert from Python to JSON:

import json

# a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)


# Convert Python objects into JSON strings, and print the values:

import json

print(json.dumps({"name": "John", "age": 30}))
print(json.dumps(["apple", "bananas"]))
print(json.dumps(("apple", "bananas")))
print(json.dumps("hello"))
print(json.dumps(42))
print(json.dumps(31.76))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))


# Python	JSON
# dict	Object
# list	Array
# tuple	Array

# str	String
# int	Number
# float	Number
# True	true
# False	false
# None	null


# In the example above, the user had to input their name on a new line. The Python input() function has a prompt parameter, which acts as a message you can put in front of the user input, on the same line:

# Example
# Add a message in front of the user input:

# name = input("Enter your name:")
# print(f"Hello {name}")

# Multiple Inputs
# You can add as many inputs as you want, Python will stop executing at each of them, waiting for user input:


# name = input("Enter your name:")
# print(f"Hello {name}")
# fav1 = input("What is your favorite animal:")
# fav2 = input("What is your favorite color:")
# fav3 = input("What is your favorite number:")
# print(f"Do you want a {fav2} {fav1} with {fav3} legs?")

# Input Number
# The input from the user is treated as a string. Even if, in the example above, you can input a number, the Python interpreter will still treat it as a string.

# You can convert the input into a number with the float() function:

# Example
# To find the square root, the input has to be converted into a number:

# x = input("Enter a number:")

#find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}")

# Validate Input
# It is a good practice to validate any input from the user. In the example above, an error will occur if the user inputs something other than a number.

# To avoid getting an error, we can test the input, and if it is not a number, the user could get a message like "Wrong input, please try again", and allowed to make a new input:

# Example
# Keep asking until you get a number:


# y = True
# while y == True:
#   x = input("Enter a number:")
#   try:
#     x = float(x);
#     y = False
#   except:
#     print("Wrong input, please try again.")

# print("Thank you!")

# The try block lets you test a block of code for errors.

# The except block lets you handle the error.

# The else block lets you execute code when there is no error.

# The finally block lets you execute code, regardless of the result of the try- and except blocks.

# Exception Handling
# When an error occurs, or exception as we call it, Python will normally stop and generate an error message.

# These exceptions can be handled using the try statement:

# ExampleGet your own Python Server
# The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")



# You can define as many exception blocks as you want, e.g. if you want to execute a special block of code for a special kind of error:

# Example
# Print one message if the try block raises a NameError and another for other errors:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")


# The finally block, if specified, will be executed regardless if the
#  try block raises an error or not.


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")