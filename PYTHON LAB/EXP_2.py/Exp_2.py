# Write a Program where the radius is taken as input to compute the area of a circle. 
import math  #for the value of pi
radius = int(input("Enter the radius of the circle: "))
area = math.pi * radius**2   # ** is for exponentiation
print(f"The area of the circle with radius {radius} is: {area}")

