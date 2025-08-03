# You can evaluate any expression in Python, and get one of two answers, True or False.

print(11>9)
print(23<17)
print(10==10)

# Print a message based on whether the condition is True or False:
x =8;
y=29;

if(x<y):
    print("y is greater than x");
else:
    print("y is not greater than x");


# Evaluate a string and a number:

print(bool("Hello"))
print(bool(15))

# Evaluate two variables:

x = "Hello"
y = 15

print(bool(x))
print(bool(y))



# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# Example
# The following will return True:

print(bool("abc"))
print(bool(0))
print(bool(["apple", "cherry", "banana"]))


# The following will return False:

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# Print "YES!" if the function returns True, otherwise print "NO!":

def myFunc():
    return True;

if myFunc():
    print("YES!");
else:
    print("NO!!");


# Python also has many built-in functions that return a boolean value, like the isinstance() function, which can be used to determine if an object is of a certain data type:

# Example
# Check if an object is an integer or not:

a=400;
print(isinstance(a,float));