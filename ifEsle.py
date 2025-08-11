# Python supports the usual logical conditions from mathematics:

# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b

x=5;
y=9;
if y>x:
    print("y is greater than x");

a = 33
b = 33
if b > a:
  print("b is greater than a");
elif a==b:
   print("a and b are equal ");
else:
   print("None of  conditions matches!")

p=6;
q=5;
if q>p:
   print("q is greater than p");
else:
   print("q is not greater the p")


# Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500

if a>b and c>a:
   print("Both conditions are true");
else:
   print("None of the conditon are true");


# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500

if a>b or a>c:
   print("At least one of the conditions is true");
else:
   print("Default condition")


# Test if a is NOT greater than b:

a = 33;
b=200;
if(not a>b):
   print("a is not greater than b");
else:
   print("Not condition checked")

# Nested if
a=50;
if a>20:
   print("a is Above ten ")
   if a>40:
      print("and also above 40");
   else:
      print("but not above 40");
else:
   print("none of the condition are match!!")


# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

a = 33
b = 200

if b > a:
  pass

# The match statement selects one of many code blocks to be executed.

# match expression:
#   case x:
#     code block
#   case y:
#     code block
#   case z:
#     code block
# This is how it works:

# The match expression is evaluated once.
# The value of the expression is compared with the values of each case.
# If there is a match, the associated block of code is executed.
# The example below uses the weekday number to print the weekday name:

day =5;
match day:
   case 1:
      print("Saturday")
   case 2:
      print("Sunday")
   case 3:
      print("Monday")
   case 4:
      print("Tuesday")
   case 5:
      print("Wednesday")
   case 6:
      print("Thursday")
   case 7:
      print("Friday")

# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")


# Combine Values
# Use the pipe character | as an or operator in the case evaluation to check for more than one value match in one case:

day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!");


# If Statements as Guards
# You can add if statements in the case evaluation as an extra condition-check:

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")