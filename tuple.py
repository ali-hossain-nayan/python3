# python tuples 
# Tuples are used to store multiple items in a single variable.
myTuple=("apple","banana","orange");
print(myTuple)

# Tuple Items
# Tuple items are ordered, unchangeable, and allow duplicate values.
# Tuple items are indexed, the first item has index [0], 
# the second item has index [1] etc.

# Unchangeable 
# Tuples are unchangeable, meaning that we cannot change, add or 
# remove items after the tuple has been created.


# Allow Duplicates
# Since tuples are indexed, they can have items with the same value:

# Example
# Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
print(len(thistuple)) 

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after 
# the item, otherwise Python will not recognize it as a tuple.
# One item tuple, remember the comma:

thistuple = ("apple",)
print(type(thistuple))#tuple have to put camera

#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) #type string

# A tuple with strings, integers and boolean values:

tuple1 = ("abc", 34, True, 40, "male")


# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Print the second item in the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Print the last item of the tuple:

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new tuple with the specified items.

# Example
# Return the third, fourth, and fifth item:

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

if "apple" in thistuple:
    print("Yes, 'apple is in the fruitlist' ")
else:
    print("No 'Its not in the list' ")


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.

x=("apple","orange","cherry")
y=list(x)
y[1]="kiwi"
x=tuple(y)

print(x)

#Add Items
thistuple = ("apple", "banana", "cherry")
convertToList = list(thistuple)
convertToList.append("orange");
thistuple=tuple(convertToList)
print(thistuple)


# Add tuple to a tuple. You are allowed to add tuples to tuples,
# so if you want to add one item, (or many), create a new tuple with 
# the item(s), and add it to the existing tuple:

anotherTuple=("gueava","Licchi")
thistuple += anotherTuple
print(thistuple)

# remvoe Items
thistuple=("apple", "banana", "cherry")
convertToList = list(thistuple)
convertToList.remove("banana")
thistuple=tuple(convertToList)
print(thistuple)


# delete the tuple completely
thistuple=("apple", "banana", "cherry")
del thistuple
# print(thistuple)

# Unpacking a Tuple
# When we create a tuple, we normally assign values to it.
# This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")

# But, in Python, we are also allowed to extract the values back into variables.
# This is called "unpacking": like destructuring
fruits = ("apple", "banana", "cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, 
# you can add an * to the variable name and 
# the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

# If the asterisk is added to another variable name than the last,
# Python will assign values to the variable until the number of values 
# left matches the number of variables left.
# like give every variable at least one value and take remaining for himself *
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green,*yellow,red,orange)=fruits
print(green)
print(yellow)
print(red)
print(orange)

# loop through for loop
thistuple = ("apple", "banana", "cherry")
for i in thistuple:
    print(i)

# Loop Through the Index Numbers
# You can also loop through the tuple items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable.

# Example
# Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])

# You can loop through the tuple items by using a while loop.
# Use the len() function to determine the length of the tuple, 
# then start at 0 and loop your way through the tuple items by referring 
# to their indexes.
# Remember to increase the index by 1 after each iteration.

thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
i=0
while i<len(thistuple):
    print(thistuple[i])
    i +=1

# To join two or more tuples you can use the + operator:

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

# Multiply Tuples
# If you want to multiply the content of a tuple a given number
# of times, you can use the * operator:
thistuple = ("apple", "banana", "cherry", "strawberry", "raspberry")
myNewTuple=thistuple * 2
print(myNewTuple)

