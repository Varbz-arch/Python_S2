# A class is a blueprint for creating objects (instances). 
# It defines properties (variables) and behaviors (methods) 
# that the objects created from the class will have.

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed

#     def bark(self): #bark is method
#         print(f"{self.breed} is barking!")
#         return f"Point is({self.name})"
#         # print(f"{self.name} is ordering!")       
# # Object: An instance of a class.
# # Creating an object: Instantiate the class to create an object.
# dog1 = Dog("Buddy", "Golden Retriever")
# dog1.bark()

# # To see the returned value, you can print it explicitly
# returned_value = dog1.bark()  # This will print the breed and return the string
# print(returned_value) 
# Methods are functions defined within a class. They describe the behaviors of objects.
# The first parameter of a method is usually self, which refers to the instance of the class.

# The constructor method (__init__) is a special method 
# that is called when an object is instantiated. 
# It's used to initialize the object's attributes.

# Special methods (also called dunder methods) are predefined methods in Python,
# prefixed and suffixed with double underscores (__), used to implement operations
#  like addition, string representation, etc.
# class Point:
#     def __init__(self, x, y):
#         self.x = x 
#         self.y = y
#     def __str__(self):
#         return f"Point is({self.x}, {self.y})"
# p1 = Point(2, 3)   #p1 is the class ob
# print(p1)  # Output: Point(2, 3) 

# Class variables are shared by all instances of the class.
# Object variables are specific to each instance.

# Public: Accessible from anywhere.
# Private: Prefixed with two underscores (__), these are not directly accessible outside the class.
# class Person:
#     age = 15  # class variable
#     def __init__(self, name, age=None):
#         self.name = name
#         # If no age is provided, use the class variable
#         if age is None:
#             self.__age = Person.age   # using the class variable
#         else:
#             self.__age = age           # use provided age
#     def get_age(self):
#         print(f"{self.name} and {self.__age}")
#         return self.__age
# # Creating object without giving age
# person1 = Person("Archisha")
# person1.get_age()  # will use class variable age = 15
# # Creating object with giving age
# person2 = Person("Anika", 22)
# person2.get_age()  # will use age = 22

#built in attributes like __doc__ or __name__
# class Dog:
#     """DOCSTRING YEAA"""
#     pass
# print(Dog.__name__)  # Output: Dog
# print(Dog.__doc__)   # Output: None (if not defined)

# Python uses garbage collection to automatically manage memory.   __del__
# It automatically frees memory when objects are no longer in use.
# class MyClass:
#     def __del__(self):
#         print("Object is being deleted")

# An abstract class used as a blueprint for other classes. 
# It can contain abstract methods (methods without implementation) which must be implemented by subclasses.
# from abc import ABC, abstractmethod
# class Animal(ABC):
#     @abstractmethod
#     def sound(self):
#         pass

# class Dog(Animal):
#     def sound(self):
#         return "Woof"

# Inheritance allows one class to inherit attributes 
# and methods from another class. This promotes code reuse.
# class Animal:  #base class
#     def eat(self): #a method eat inside the class
#         print("Eating")
# class Dog(Animal): #Creating a child class Dog that inherits from Animal
#     def bark(self): #a new method inside the dog class
#         print("Barking")
# #The Dog class automatically gets all the features (methods/variables) from Animal.
# d=Dog() #create an object from dog class
# d.eat() #inherited from animal
# d.bark() #own method of dog

#basically, it was child gets all properties or methods of parents
# Single Inheritance: A subclass inherits from a single class.
# Multiple Inheritance: A subclass inherits from more than one class.
# Multilevel Inheritance: A subclass inherits from a superclass, and that superclass inherits from another class.
# Hierarchical Inheritance: Multiple subclasses inherit from a single superclass.
# Hybrid Inheritance: A combination of multiple types of inheritance.

# Polymorphism allows for methods to behave differently based on the object that is calling them.
#  it allows the same method name to behave differently depending on the object that calls it.
#operator overloading
# class Point:
#     def __init__(self, x, y):  #when an object is created
#         self.x = x #set x as instance of point
#         self.y = y
#     def __add__(self, other):  #self as current object and other as second object
#         return Point(self.x + other.x, self.y + other.y)
#     def __str__(self):   # defines how the object should be represented as a string when passed to print().
#         return f"point is ({self.x},{self.y})"
# p1 = Point(1, 2)  #self
# p2 = Point(3, 4)  #other
# p3 = p1 + p2  # Calls __add__ method
# print(p3) #without str, it will define something else

# #overidden
# When you want to modify or extend the behavior of a method 
# that is already defined in the parent class.
# class Animal:
#     def speak(self):
#         print("Animal is making a sound")
# class Dog(Animal):
#     def speak(self):  # Overriding the parent's speak method
#         print("Dog is barking")
# class Cat(Animal):
#     def speak(self):  # Overriding the parent's speak method
#         print("Cat is meowing")
# # Create objects
# animal = Animal()
# dog = Dog()
# cat = Cat()
# # Calling the overridden method on different objects
# animal.speak()  # Calls parent class method
# dog.speak()     # Calls child class (Dog) method
# cat.speak()     # Calls child class (Cat) method


