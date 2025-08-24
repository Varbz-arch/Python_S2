#Write a program to swap two numbers without taking additional variable. 

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
temp=a
a=b
b=temp
print(f"After swapping: a = {a}, b = {b}")

