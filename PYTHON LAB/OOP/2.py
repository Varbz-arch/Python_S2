class Person:
    def __init__(self):
        self.name = "Archisha"  # Name is fixed inside the class
    def greet(self):
        print("Hello, my name is", self.name)
p = Person()
p.greet()
# the difference
class Person:
    def __init__(self, name): #expexts name to be passed in when creating an obj like p
        self.name = name    # Name is given from outside

    def greet(self):
        print("Hi, I'm", self.name)
p1 = Person("Archisha")
p2 = Person("Archi")

p1.greet()  
p2.greet() 
