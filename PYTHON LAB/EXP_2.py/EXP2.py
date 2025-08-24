#1
''' Declare these variables (x, y and z) as integers. Assign a value of 9 to x, Assign 
a value of 7 to y, perform addition, multiplication, division and subtraction on 
these two variables and Print out the result.''' 

x = 9
y = 7
addition = x + y
subtraction = x - y
multiplication = x * y
division = x // y  # //-> integer division  /-> float division
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

#2
# Write a Program where the radius is taken as input to compute the area of a circle. 
import math  #for the value of pi
radius = int(input("Enter the radius of the circle: "))
area = math.pi * radius**2   # ** is for exponentiation
print(f"The area of the circle with radius {radius} is: {area}")

#3
''' Write a Python program to solve (x+y)*(x+y) 
Test data : x = 4 , y = 3 
Expected output: 49 '''

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
result = (x + y) * (x + y)
print(f"The result of (x + y) * (x + y) where x = {x} and y = {y} is: {result}")

#4
''' Write a program to compute the length of the hypotenuse (c) of a right triangle 
using Pythagoras theorem. '''

import math  
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = math.sqrt(a**2 + b**2)
print(f"The length of the hypotenuse is: {c}")

#5
#Write a program to find simple interest.

P = int(input("Enter the principal amount (P): "))
R = int(input("Enter the rate of interest (R): "))
T = int(input("Enter the time period (T) in years: "))
simple_interest = (P * R * T) / 100
print(f"The simple interest is: {simple_interest}")

#6
#Write a program to find area of triangle when length of sides are given. 

import math  
a = int(input("Enter the length of side a: "))
b = int(input("Enter the length of side b: "))
c = int(input("Enter the length of side c: "))
# semi-perimeter
s = (a + b + c) / 2
# Heron's formula
area = math.sqrt(s * (s - a) * (s - b) * (s - c)) #sqrt-square root
print(f"The area of the triangle is: {area}")

#7
# Write a program to convert given seconds into hours, minutes and remaining 
# seconds. 

seconds = int(input("Enter the number of seconds: "))
hours = seconds // 3600
minutes = (seconds % 3600) // 60
remaining_seconds = seconds % 60
print(f"{seconds} seconds is equivalent to {hours} hours, {minutes} minutes, and {remaining_seconds} seconds.")

#8
#Write a program to swap two numbers without taking additional variable. 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
temp=a
a=b
b=temp
print(f"After swapping: a = {a}, b = {b}")

#9
#Write a program to find sum of first n natural numbers.

n = int(input("Enter a number n: "))
sum = (n * (n + 1)) // 2
print(f"The sum of the first {n} natural numbers is: {sum}")

#10
#Write a program to print truth table for bitwise operators( & , | and ^ operators) 

print("A B  A&B  A|B  A^B")
for A in [0, 1]:
    for B in [0, 1]:
        AND = A & B
        OR = A | B
        XOR = A ^ B
        print(f"{A} {B}   {AND}   {OR}   {XOR}")

#11
# Write a program to find left shift and right shift values of a given number. 

n = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))
left_result = n << shift
right_result = n >> shift
print(f"The result of left shift {n} by {shift} positions is: {left_result}")
print(f"The result of right shift {n} by {shift} positions is: {right_result}")

#12
#Using membership operator find whether a given number is in sequence (10,20,56,78,89) 

sequence={10,20,56,78,89}
n=int(input("Enter the number to check whether the number is in sequence or not:"))
if n in sequence:
    print(f'{n} is in the sequence')
else:
    print(f'{n} is not in the sequence')

#13
# Using membership operator find whether a given character is in a string. 

NAME='AVINASH'
if 'A' in NAME:
    print('EXISTS')
else:
    print('TRY AGAIN')
