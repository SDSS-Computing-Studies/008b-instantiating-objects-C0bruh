#!python3

"""
Why have a class/object instead of a single program. That's because sometimes
we might want to have multiple objects!

Remember, each object has its own copy of all the class properties and 
methods, and all of the properties have the same name, so how do we
distinguish between them?  By the use of a prefix!

Note that the prefix does not have to be a variable. We can have a list 
of objects!
"""

class car:
    make = None
    model = None
    year = None
    value = None

    def __init__(self):
        print("\n")
        self.make = input("Enter the make of your car:")
        self.model = input("What model car is this:")
        self.year = int(input("What is the year of manufacture:"))
        self.value = int( input("What is the new value of this car:"))
    
    def displayCar(self):
        output = str(self.year) + " " + self.make + " " + self.model
        outputLength = len(output)
        print( outputLength * "=")
        print( output)
        print( outputLength * "=")

    def curvalue(self,currentYear):
        # function to determine the current value of the car
        # the current value is based on the age of the car and 
        # the initial value
        difference = currentYear - self.year
        curVal = self.value*(0.9)**difference
        loss = self.value - curVal
        self.displayCar()
        print("Current Value is " + str(curVal))
        print("Your car has depreciated " + str(loss))


# an empty list for the cars to be stored in has been created
cars = []

# for loop has been created so that we can enter in multiple cars
for i in range(0,3):
    # we append some cars to the list.  The cars are instantiated
    # by calling the car() class as a function. It will execute
    # the code in its constructor
    cars.append( car() )


# the list is now a list of objects.  Each element is an object
# and we can use the list with its index to access object properties
# or methods
print( cars[0].make )
print( cars[1].curvalue() )
s
