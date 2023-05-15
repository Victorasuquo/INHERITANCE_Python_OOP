#INHERITANCE IN PYTHON OOP
"----------------------------------------------------------------------"    

#What is INHERITANCE IN PYTHON PROGRAMMING
"""
     Inheritance is a 
Any object bound to a specific level of hierachy inhrits all the traits (as well as the attributes 
 and qualities) defined inside any of the Superclass. Just like people, have parents, gran parents
 and so on, objects have ancesstory. The principle of Inheritance lets a programmer to build
 reationships bewteen concepts an group them together. In particuler this alows us to avoid
code duplicatioin by generalizing our code. 

In python we use parenthesis and class decaration to show an inhertane relationship 


"""
# What does an object have
"""
    The object Orineted Programming Assumes that every existing object may be equipped with three
groups of attributed.
- an object has a name
- an object has a sset of individual properties or attributes.
- an object has a setr of abilities to perform specific task, change the object itself,
  etc(Methods)

  
#Attributes are characteristics associated with a type.
Methods are functons associated with a type.  To list all the attributes and methods of a class 
- use dir("") function
- help("") function to show all the documentation
"""

#objects can be organised by inheritance()
#EXAMPLE
"""
We can generalise our class to be the vehicle class
class Vehicle

"""
   
class Fruit:
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor

class Grape(Fruit):
    pass

class Apple(Fruit):
    pass
#we told python to inherit all the methods and functions from the Base Class or 
# super Class "Fruit"
 
Granny_smith = Apple("green", "tart")
carnelian = Grape("purple", "sweet")

print(carnelian.color)
print(Granny_smith.flavor)


class Animal:
    sound = ""
    def __init__(self, name):
        self.name = name
    def speak(self):
        print("{sound}, I am {name}, {sound}".format(name = self.name, sound = self.sound))



class piglet(Animal):
    sound = "oink !"
hamlet = piglet("harmlet")
hamlet.speak()

# Python code to demonstrate how parent constructors
# are called.
"""
Inheritance
Inheritance is the capability of one class to derive or inherit the properties from 
another class.
The class that derives properties is called the derived class or child class and the class from
which the properties are being derived is called the base class or parent class or super class.

The benefits of inheritance are:

-It represents real-world relationships well.
-It provides the reusability of a code. We don’t have to write the same code again and again. 
-Also, it allows us to add more features to a class without modifying it.
-It is transitive in nature, which means that if class B inherits from another class A, then all
 the subclasses of B would automatically inherit from class A.

Types of Inheritance – 
Single Inheritance:
Single-level inheritance enables a derived class to inherit characteristics from a single-parent 
class.

Multilevel Inheritance:
Multi-level inheritance enables a derived class to inherit properties from an immediate parent 
class which in turn inherits properties from his parent class.

Hierarchical Inheritance:
Hierarchical level inheritance enables more than one derived class to inherit properties from a 
parent class.

Multiple Inheritance:
Multiple level inheritance enables one derived class to inherit properties from more than one 
base class.

Example: Inheritance in Python
"""

# parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
	
# child class
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using
# its instance
print(a.display())
print(a.details())


# Output
# Rahul
# 886012
# My name is Rahul
# IdNumber: 886012
# Post: Intern
"""In the above code, we have created two classes i.e. Person (parent class) and Employee 
(Child Class). The Employee class inherits from the Person class. We can use the methods of the
 person class through employee class as seen in the display function in the above code. 
 A child class can also modify the behavior of the parent class as seen through the details()
method."""