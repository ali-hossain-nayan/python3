# string
x = "Hello World"
print(x)

# integer
x = 5
print(x)
# float
x = 5.5
print(x)
# complex number
x = 5j
print(x)
# list # in js its array
x = ["apple", "banana", "cherry"]
print(x)
# tuple
x = ("apple", "banana", "cherry")
print(x)
# range
x = range(6)
print(x)
# dict in js its object
x = {"name": "John", "age": 30}
print(x)
# set # in js its set
x = {"apple", "banana", "cherry"}
print(x)
print(type(x))

# You can convert from one type to another with the int(), float(),
#  and complex() methods:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


# Python Casting
# There may be times when you want to specify a type on to a variable.
# This can be done with casting. Python is an object-orientated language, and as such it uses
#  classes to define data types, including its primitive types.


x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
