# List
# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, 
# the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

# Lists are created using square brackets: like array in js

list1=["apple","orange","cherry"];
print(list1);

# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# Example
# Lists allow duplicate values:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

# Print the number of items in the list:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# A list can contain different data types:

# Example
# A list with strings, integers and boolean values:

list1 = ["abc", 34, True, 40, "male"]

# What is the data type of a list?

mylist = ["apple", "banana", "cherry"]
print(type(mylist))


# Access items
print(mylist[2])

# Range of Indexes
# You can specify a range of indexes by specifying where to start and where to end the range.

# When specifying a range, the return value will be a new list with the specified items.

# Example
# Return the third, fourth, and fifth item:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


# This example returns the items from the beginning to, but NOT including, 

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


# This example returns the items from "cherry" to the end:

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

if "appl" in thislist:
    print("Yes apple in the fruits list");
elif "chery" in thislist:
    print("Yes cherry in the fruits list");
else:
    print("given name isn't in the fruits list");


# Change the second item:

thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist);

thislist[1:3]=["blackcurrant","walermelon"]
print(thislist);

# If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second value by replacing it with two new values:

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist);


# If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:

# Example
# Change the second and third value by replacing it with one value:

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist);

# Insert Items
# To insert a new list item, without replacing any of the existing values, we can use the insert() method.

# The insert() method inserts an item at the specified index:

# Example
# Insert "watermelon" as the third item:

thislist = ["apple", "banana", "cherry"]
thislist.insert(2,"lemon")
print(thislist);

# Append Items
# To add an item to the end of the list, use the append() method:

# ExampleGet your own Python Server
# Using the append() method to append an item:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist);

# Extend List
# To append elements from another list to the current list, use the extend() method.

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical);
print(thislist);

# Add Any Iterable
# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).

# Example
# Add elements of a tuple to a list:

thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple);
print(thislist);


# Remove Specified Item
# The remove() method removes the specified item.

# ExampleGet your own Python Server
# Remove "banana":

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)


# Remove the first occurrence of "banana":

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# Remove Specified Index
# The pop() method removes the specified index.

# Example
# Remove the second item:

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist);

# If you do not specify the index, the pop() method removes the last item.

# Example
# Remove the last item:

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist);

# The del keyword also removes the specified index:

# Example
# Remove the first item:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist);

# The clear() method empties the list.

# The list still remains, but it has no content.

# Example
# Clear the list content:

thislist = ["apple", "banana", "cherry"]
# thislist.clear()
print(thislist);

# loop all items
for x in thislist:
    print(x);

for x in range(len(thislist)):
    print("Using range list " + thislist[x]);

x=0;
while x<len(thislist):
    print(thislist[x])
    x +=1;


# List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:

fruits =["apple","banana","orange","cherry", "kiwi","licchi"];
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x);
print(newlist);


# With list comprehension you can do all that with only one line of code:
#
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


# Sort the list alphabetically:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)


# Sort the list numerically:

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
# sort the list descending
thislist.sort(reverse=True);
print(thislist);

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse=True)
print(thislist);

# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

# Example
# Sort the list based on how close the number is to 50:

def myfunc(n):
    return abs(n-50);


thislist = [100, 50, 65, 82, 23]
thislist.sort(key=myfunc)
print(thislist)

# myfunc(n) returns the absolute difference between n and 50.

# thislist.sort(key=myfunc) tells Python to sort the list not by the numbers themselves, but by the value returned from myfunc.

# So Python will calculate:

# abs(100 - 50) = 50

# abs(50 - 50) = 0

# abs(65 - 50) = 15

# abs(82 - 50) = 32

# abs(23 - 50) = 27

# Now it sorts based on these values:

# 50 (for 100)

# 0 (for 50)

# 15 (for 65)

# 32 (for 82)

# 27 (for 23)


# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example
# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist);

# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist);

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist);

# Copy a List
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# Use the copy() method
# You can use the built-in List method copy() to copy a list.

# ExampleGet your own Python Server
# Make a copy of a list with the copy() method:

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist);


# Use the list() method
# Another way to make a copy is to use the built-in method list().

# Example
# Make a copy of a list with the list() method:

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist);

# Join two list:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3);

for i in list2:
    list1.append(i);
print(list1);

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)


# List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list