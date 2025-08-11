# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.


def myFunction():
    print("This is function");

myFunction();


# Information can be passed into functions as arguments.

def myFunction2(firstName):
    print(firstName + " Hoxn");

myFunction2("Ali");
myFunction2("Linus");


# By default, a function must be called with the correct number
#  of arguments. Meaning that if your function expects 2 arguments,
#  you have to call the function
#  with 2 arguments, not more, and not less.
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil" , "Refsnes")


# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
  print("The youngest child is " + kids[0])

my_function("Emil", "Tobias", "Linus")


# You can also send arguments with the key = value syntax.
# This way the order of the arguments does not matter.

def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



# If we call the function without argument, it uses the default value:
def myFunction (country="Norway"):
   print("I am from " + country);

myFunction()
myFunction("Swiden")
myFunction("Russia")



# You can send any data types of argument to a function 
# (string, number, list, dictionary etc.), and it will be treated
#  as the same data type inside the function.
def myFunction(food):
   print(food);

fruits = ["apple","banana","cherry"]
myFunction(fruits);



def myFunction(food):
   for i in food:
      print(i);
fruits = ["kola","komola", "Anaros"];
myFunction(fruits);


def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))


# function definitions cannot be empty, but if you for some reason
#  have a function definition with no content, put in the pass
#  statement to avoid getting an error.

def myfunction():
  pass



# Recursion
# Python also accepts function recursion, which means a defined function 
# can call itself.

# Recursion is a common mathematical and programming concept. 
# It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

# The developer should be very careful with recursion as it can be
#  quite easy to slip into writing a function which never terminates, 
# or one that uses excess amounts of memory or processor power. However,
#  when written correctly recursion can be a very efficient and 
# mathematically-elegant approach to programming.

# In this example, tri_recursion() is a function that we have defined
#  to call itself ("recurse"). We use the k variable as the data, 
# which decrements (-1) every time we recurse. The recursion ends 
# when the condition is not greater than 0 (i.e. when it is 0).

# To a new developer it can take some time to work out how exactly 
# this works, best way to find out is by testing and modifying it.


def tri_recursion(n):
   if(n>0):
      result = n + tri_recursion(n-1)
      print(result);
   else:
      result = 0;
   return result;

print("Recursion example results")
tri_recursion(8)