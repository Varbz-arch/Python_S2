# class Student:
#     def __init__(self, name, sapid, state):
#         self.name=name
#         self.sapid=sapid
#     def student_info(self):
#         print(f"The name of the student with sapid {self.sapid} is {self.name} from {self.state}")
#     name= 'Archisha'
#     sapid='18066'
#     state='Uttarakhand'
# S1=Student('Archisha', 18066, 'Uttarakhand')
# S1.student_info()

# class University:
#     def __init__(self, name, sapid, state):   #__init__ is constructor
#         print("object got created")
#         self.name = name
#         self.sapid = sapid
#         self.state = state
#     def student_info(self):
#         print(f"{self.name} with {self.sapid} and from {self.state} is marked today")
#     def __str__(self):
#         return 'University object'
# student1 = University('Archisha', 18066, 'Uttarakhand')
# student2 = University('Archi', 5900 , 'Assam')
# student1.student_info()
# student2.student_info()
# print()
# U1=University("Heyyyaaaa", 2000, "Assam")
# print(U1)

# class Student(University):  # This defines a child class Student that inherits from University.
#     S1=University("Atul", 2000, "JK")   #s1 is class variable
#     S1.student_info()

# class Teacher(University):  #Teacher inherits from University.
#     def __init__(self, name, sapid, state, salary):  #4 parameters
#         super(). __init__( name, sapid, state)  #Inherit all the parent class's initialization 
#                                                 #  and Avoid repeating the self.name = ...
#         # (self, name, ...., salary)
#         self.salary=salary   #self.__salary=salary means u cannot access this variables outside the class
#     def display_impinfo(self):
#         print(f"The name of salary of the employee with sapid is {self.sapid} is {self.name} and {self.salary}")
# Hankes= Teacher ("xyz", 5900, "JK", "520K")
# Hankes.display_impinfo()

# super()	Calls parent class constructor to avoid rewriting same code

# a=2
# b=3
# c=10
# a=5
# print(a)  #overwrite

# a.length? it works in other programming language and not in python and if its in python, its len(a)
# class MyData:
#     def __init__(self, data):
#         self.data = data

#     def __len__(self):    # special built in methods
#         return len(self.data)

# a = MyData([1, 2, 3])
# b = MyData([2,2,2,5,5])
# print("number of elements is",  len(a)) 
# print("number of elements is",  len(b)) 

#pass?    is used when you want to do nothing in a block of code. "placeholder"
# example 1
# def placeholder_function():
#     pass  # Function does nothing for now

# placeholder_function()

# example 2
# class MyClass:
#     pass  # Class is currently empty
 
# or loop

# @property   reaf only attribute
# class MyClass:
#     def __init__(self, value):
#         self._value = value  # private attribute (underscore is a convention)

#     @property
#     def value(self):
#         return self._value
    
# obj = MyClass(10)
# print(obj.value)

# @abstractmethod    abstract base classes (ABCs), which allow you to define 
# a method in a base class that must be implemented by any subclass

# def last_working_day():
#     pass
#from able import ABC, abstractmethod
#and at top, class University(ABC)

# 2 TYPES OF inheritance types
# 1. Multilevel  a-> b-> c  
#               class b(a)
#               class c(b)
# Base class
# class A:
#     def __init__(self):
#         print("Class A")
# # Class B inherits from A
# class B(A):
#     def __init__(self):
#         super().__init__()  # Calling the constructor of class A
# # The super() function is used to call methods from a parent class
# #  (also called the superclass) in a child class (also called the subclass)
#         print("Class B")
# # Class C inherits from B, which in turn inherits from A
# class C(B):
#     def __init__(self):
#         super().__init__()  # Calling the constructor of class B
#         print("Class C")
# # Create an object of class C
# obj = C()

# 2. multiple
#         class Child (Father, mother)
#         class X(a,b,c,d)
# Parent class Father
# class Father:
#     def __init__(self):
#         self.father_name = "John"
#         print("Father class initialized")
#     def speak_father(self):
#         print("I am your father.")
# # Parent class Mother
# class Mother:
#     def __init__(self):
#         self.mother_name = "Sarah"
#         print("Mother class initialized")

#     def speak_mother(self):
#         print("I am your mother.")
# # Child class inherits from both Father and Mother
# class Child(Father, Mother): #hence, multiple
#     def __init__(self):
#         Father.__init__(self)  # Calling constructor of Father
#         Mother.__init__(self)  # Calling constructor of Mother
#         print("Child class initialized")
#     def speak_child(self):
#         print("I am the child!")
# # Create an object of class Child
# child = Child()
# child.speak_father()  # Inherited from Father
# child.speak_mother()  # Inherited from Mother
# child.speak_child()   # Method of the Child class

# class A:
#     total_students=0
#     def __init__(self):
#         ....
#     def student_info(self):
#         ....
# A.total_students
