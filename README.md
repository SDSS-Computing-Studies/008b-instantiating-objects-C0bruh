## SDSS Computing Studies Python Assignment
### Assignment #008b Using Classes and Their Methods
Objectives:
* Create a function call to a class method
* Create your own instances from a class
* Begin using 'properties' instead of 'variables' when referring to objects
* Begin using 'methods' instead of 'functions' when referring to objects

Once you create a class, you've really only created a template.
Just like creating the IDEA of a car, a class doesn't really 
exist as a program until you actually instantiate it.

Today we will follow some examples to illustrate some of the ways
that we can make use of classes and how the methods and properties
can be referenced.

example1.py
Class methods an properties can actually be used without
instantiation, but the functionality is limited, as the
class properties can not be changed.  Only an object can
have its properties differ from the class "template"

example2.py
A class is really just a template or idea.  When we
create an instance, we are creating an object, that has
its own properties and methods.  This shows how
an object is instantiated and how we can access
object properties and methods

example3.py
Multiple objects can be instantiated.  Each has their
own copy of the class properties and methods, so using
the name and dot notation can help distinguish between
which object we are talking about.

### 1 Tasks

##### Task 1
Create a class that will store a database for a veterinarian.
Your class will need the following properties:

animal (dog, cat, fish, bird, turtle, etc)
breed
name (the pet's name)
owner (the owner's name)
birthdate (of the pet, expressed as yyyy-mm-dd)

The constructor will need to ask for each of those values
for the database when the pet is instantiated

Methods:
display() - should show the name of the pet and type followed by their breed and owner


Main block should have a menu that has the following options:
1. Enter a new pet
2. Retrieve a pet
3. Exit

If they choose to retrieve a pet,
display the following:
Enter pet's name:
and then go through the list, looking for the name of the pet.
If the pet is found, it should call the display() method from the object

Example output:

1. Enter a new pet
2. Retrieve a pet
3. Exit
1

Type of animal? dog
Breed? Shih-tzu
Name? Buster
Owner? Christy
Birthdate? 2008-10-16

1. Enter a new pet
2. Retrieve a pet
3. Exit
2

Which Pet? Buster

Buster dog
Shih-tzu is owned by Christy
(10 points) 

