#!python3

"""
When a class is assigned to a variable, it is instantiated.
An object is created, and the name of the object is the variable
name that it is assigned to.  It inherits all of the properties and
methods (variables and functions) that are defined in the class template.

To access the object's properties and methods, we use dot notation,
with the variable as a prefix before the dot, and the object properties
and methods after the dot.
"""

class test:
    var1 = "this is var1"
    var2 = "this is var2"

    def __init__(self):
        print("--")
        print("the class has been instantiated")

    def __del__(self):
        print("The class has been destroyed")
        print("--")
    
    def function1(self):
        print("this is a function!")

"""
To instantiate an object, we assign it to a variable.  Note that it will
require any input parameters that the constructor requires
"""
x = test()

# to access object properties, we use the dot notation, with the
# prefix being the variable name that the object is stored in, and the
# object property listed after the dot
print("The value of x.var1 is ", end="")
print( x.var1 )

# Note that once an object is instantiated, we can change assign new
# values to the properties just by assigning a variable
x.var1 = "New Value"
print("The value of x.var1 is ", end="")
print( x.var1 )


# Note also that the object only calls the constructor when it is
# instantiated, and then destructor only once when it is destroyed
# or the program ends
del x
