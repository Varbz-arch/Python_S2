''' Write a program to compute the length of the hypotenuse (c) of a right triangle 
using Pythagoras theorem. '''

import math  
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = math.sqrt(a**2 + b**2)
print(f"The length of the hypotenuse is: {c}")
