#Write a program to print truth table for bitwise operators( & , | and ^ operators) 

A = int(input("Enter the first number: "))
B = int(input("Enter the second number: "))
AND = A & B
OR = A | B
XOR = A ^ B
print("A B  A&B  A|B  A^B")
print(f"{A} {B}   {AND}   {OR}   {XOR}")
