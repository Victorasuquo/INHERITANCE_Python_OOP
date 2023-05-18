# #INHERITANCE IN PYTHON OOP
# "----------------------------------------------------------------------"    

# #What is INHERITANCE IN PYTHON PROGRAMMING
# """
# In heritane is a common practise (in Object Orinted Programming) of passing attributes and
#  methods from the Super class to the(defined and existing) to a ewly created class, called 
#  the sub class, sibling or child class.

# It is a mechanism that allows you to create a hierarchy of classes that share a set of 
# properties and methods by deriving a class from another class. Inheritance is the capability of
# one class to derive or inherit the properties from another class. 
# Any object bound to a specific level of hierachy inherits all the traits (as well as the attributes 
# and qualities) defined inside any of the Superclass. Just like people, have parents, grand parents
# and so on, objects have ancesstory. The principle of Inheritance lets a programmer to build
# reationships bewteen concepts an group them together. In particuler this alows us to avoid
# code duplicatioin by generalizing our code. 
 
# Parent class is the class being inherited from, also called base class or super class.

# Child class is the class that inherits from base, parent or sper class, also called derived class.
# """

# #creating a base class and a sub class
# class Vehicles:
#     pass
		
#     #base class
# class LandVehicles(Vehicles):
#       pass

# class WaterVehicles(Vehicles):
#       pass
      
# benz = LandVehicles()

# """

# The benefits of inheritance are:

# -It represents real-world relationships well and helps to build more specialised (more concrete)
# classes using some sets of predefined general rules and behaviours.

# - it is a way of buiding a new class not from scratch but by using already predefined repetoire 
#  of traits. 
#  Land
# -Also, it allows us to add more features to a class without modifying it.
# -It is transitive in nature, which means that if class B inherits from another class A, then all
#  the subclasses of B would automatically inherit from class A.

# Types of Inheritance
# Single Inheritance:
# Single-level inheritance enables a derived class to inherit characteristics from a single-parent 
# class.

# Multiple Inheritance:
# Multiple level inheritance enables one derived class to inherit properties from more than one 
# base class

# Multilevel Inheritance:
# Multi-level inheritance enables a derived class to inherit properties from an immediate parent 
# class which in turn inherits properties from his parent class.

# Hierarchical Inheritance:
# Hierarchical level inheritance enables more than one derived class to inherit properties from a 
# parent class.

# Hybrid inheritance: This form combines more than one form of inheritance. 
# Basically, it is a blend of more than one type of inheritance.

# """
# """
# #Attributes are characteristics associated with a type.
# Methods are functons associated with a type.  To list all the attributes and methods of a class 
# - use dir("") function
# - help("") function to show all the documentation
# """

# #objects can be organised by inheritance
# #EXAMPLE
# """
# We can generalise our class to be the Fruits class
# """
   
# class Fruit:
#     def __init__(self, color, flavor):
#         self.color = color
#         self.flavor = flavor

# class Grape(Fruit):
#     pass

# class Apple(Fruit):
#     pass
# #we told python to inherit all the methods and functions from the Base Class or 
# # super Class "Fruit"
 
# Granny_smith = Apple("green", "tart")
# carnelian = Grape("purple", "sweet")

# print(carnelian.color)
# print(Granny_smith.flavor)


# class Animal:
#     sound = ""
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print("{sound}, I am {name}, {sound}".format(name = self.name, sound = self.sound))



# class piglet(Animal):
#     sound = "oink !"
# hamlet = piglet("harmlet")
# hamlet.speak()

# class Cow(Animal):
# 	sound = "Moooo"
        

# milky = Cow("Milky White")
# milky.speak()
        


# # Python code to demonstrate how parent constructors
# # are called.

# #Examples of inheritance 
# # parent class
# class Person(object):

# 	# __init__ is known as the constructor
# 	def __init__(self, name, idnumber):
# 		self.name = name
# 		self.idnumber = idnumber

# 	def display(self):
# 		print(self.name)
# 		print(self.idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("IdNumber: {}".format(self.idnumber))
	
# # child class
# class Employee(Person):
# 	def __init__(self, name, idnumber, salary, post):
# 		self.salary = salary
# 		self.post = post

# 		# invoking the __init__ of the parent class
# 		Person.__init__(self, name, idnumber)
		
# 	def details(self):
# 		print("My name is {}".format(self.name))
# 		print("IdNumber: {}".format(self.idnumber))
# 		print("Post: {}".format(self.post))


# # creation of an object variable or an instance
# a = Employee('Rahul', 886012, 200000, "Intern")

# # calling a function of the class Person using
# # its instance
# print(a.display())
# print(a.details())


# # Output
# # Rahul
# # 886012
# # My name is Rahul
# # IdNumber: 886012
# # Post: Intern
# """In the above code, we have created two classes i.e. Person (parent class) and Employee 
# (Child Class). The Employee class inherits from the Person class. We can use the methods of the
#  person class through employee class as seen in the display function in the above code. 
#  A child class can also modify the behavior of the parent class as seen through the details()
# method."""



# #EDUREKA
# """the __init function is called automaticaly every time the the class is 
# used to create an object"""

# #OVER RIDDING THE SUPERCLASS
# """ we can intialize  a sub class by using the __init__() method and inherit all the
# attributes from a super class by invoking the __init__()  """


class Super_name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("This is your name " + self.name + " .")
    
class Sub(Super_name):
    def __init__(self, name):
        Super_name.__init__(self, name)
        
you = Sub("Vitor")
print(you)

"""
There is a class named Super, which defines it's own constructor used to assign the objects
property named "name". The class defines the "__str__()" method, too, which makes the class
to ba able to present it's identity in a clear text form. The class in next used as a base to 
crreate a subclass named "sub". The name Sub class defines it's own constructor, which invokes
the oe from the super class. Note, how it is done "Super.__init__(self, name).
weve explicitly named the Superclass and pointed to the method to invoke __init__(), providing
all the needed arguments. We have all instantiated one object of class sub and printed it

"""
#we cann also use the super() functio to automatically inherit all the atrributes from the 
#from the parent class which does not involve writting the Super class name

class Super_name:
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return ("This is your name " + self.name + " .")
    
class Sub(Super_name):
    def __init__(self, name):
        super().__init__(name)
        
you = Sub("Vitor")
print(you)

#more on class varibles: adding properties


class Dog:
    kennel = 0
    def _init_(self, breed):
        self.breed = breed
        Dog.kennel += 1
    def _str_(self):
        return self.breed + " says: Woof!"
 
 
class SheepDog(Dog):
    def _str_(self):
        return super()._str_() + " Don't run away, Little Lamb!"
 
 
class GuardDog(Dog):
    def _str_(self):
        return super()._str_() + " Stay where you are, Mister Intruder!"
 
 
rocky = SheepDog("Collie")
luna = GuardDog("Dobermann")
 

print(rocky)
print(luna)
 

print(issubclass(SheepDog, Dog), issubclass(SheepDog, GuardDog))
print(isinstance(rocky, GuardDog), isinstance(luna, GuardDog))


print(luna is luna, rocky is luna)
print(rocky.kennel)
 
