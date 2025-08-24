#Write a program to find area of triangle when length of sides are given. 

import math  
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c)) #sqrt-square root
print(f"The area of the triangle is: {area}")
