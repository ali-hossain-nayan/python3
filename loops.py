
# With the while loop we can execute a set of statements as long as a condition is true.
i =1;
while i<10:
    print(i)
    i=i+1;

# The while loop requires relevant variables to be ready, in this example 
# we need to define an indexing variable, i, which we set to 1.

i=1;
while i<10:
    print(i);
    if i==5:
        break;
    i =i+1;
# With the continue statement we can stop the current iteration, and continue with the next:
# Continue to the next iteration if i is 3:

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)
  

i=0;
while i<5:
   print(i)
   i = i+1
else:
   print("i is no longer less than 5");

# A for loop is used for iterating over a sequence 
# (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

# Loop through the letters in the word "banana":

for x in "banana":
  print(x);

fruits = ["apple", "banana", "cherry"]
for i in fruits:
   print(i)
   if i=="banana":
      break;
   else:
      print("Done the looping");


# Exit the loop when x is "banana", but this time the break comes before the print:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

# With the continue statement we can stop the 
# current iteration of the loop, and continue with the next:
# Do not print banana:

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

# The range() function returns a sequence of numbers, starting 
# from 0 by default, and increments 
# by 1 (by default), and ends at a specified number.
# Using the range() function:

for x in range(6):
  print(x)

# Using the start parameter:

for x in range(2, 6):
  print(x)

# Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)

# Print all numbers from 0 to 5, and print a message when the loop has ended:

for x in range(6):
  print(x)
else:
  print("Finally finished!")

# Break the loop when x is 3, and see what happens with the else block:

for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


# The "inner loop" will be executed one time for each iteration of the "outer loop":

# Example
# Print each adjective for every fruit:

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)