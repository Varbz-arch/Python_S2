#Write a program to find simple interest.

P = int(input("Enter the principal amount (P): "))
R = int(input("Enter the rate of interest (R): "))
T = int(input("Enter the time period (T) in years: "))
simple_interest = (P * R * T) / 100
print(f"The simple interest is: {simple_interest}")
