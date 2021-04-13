#!python3

"""
Class methods can actually be called without instantiation, although
class properties (variables) will have their default values, but there
is no way to change the value of the class properties or to create
new properties from within the class itself.

What actually happens is that the class is instantiated and destroyed
right away without being saved into a variable to track it.  Keep this
in mind when you are creating your constructors and destructors

Tryint to use a class without instantiating it will provide very limited
functionality.

If you are planning on using a class without instantiation
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
To call a class function without instantiation, we use the class name
as a prefix.  The prefix must include the () and any parameters that
are required by the constructor.  Any class functions can be included
after the prefix, along with any input parameters that the function might
need
"""
test().function1()


"""
Note that trying to assign a value to a class property/variable doesn't work.
The class will brielfy instantiate and destroy, but the value in the class
will not change. We can only change properties of classes if they are
instantiated
"""
test().var1 = "help!"
print( test().var1 )

# See Example 2 for simiilar tasks using instantiated objects