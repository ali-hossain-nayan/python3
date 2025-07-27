
# In Python, variables are created when you assign a value to it:
x = 5
y = "Hello, World!"
print(x)
print(y)


# Variables do not need to be declared with any particular type, 
# and can even change type after they have been set.

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0
print(x,y,z)
print(type(x), type(y), type(z))

# You can get the data type of a variable with the type() function.
x = 5
y = "John"
print(type(x))
print(type(y))

# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", 8, "Cherry"
print(x)
print(y)
print(z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x)
print(y)
print(z)

# If you have a collection of values in a list, tuple etc. 
# Python allows you to extract the values into variables. 
# This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# In the print() function, you output multiple variables, separated by a comma:
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# You can also use the + operator to output multiple variables:
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# In the print() function, when you try to combine a string and a number with the + operator, Python will give you an error:
x = 5
y = "John"
# print(x + y)

# Global Variables
# Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
print("Python is " + x)#globally accessible variable
def myfunc():
  print("Python is " + x)#accessible inside the function
myfunc()


# If you create a variable with the same name inside a function, 
# this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was,
#  global and with the original value.

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

# If you use the global keyword, the variable belongs to the global scope:

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)