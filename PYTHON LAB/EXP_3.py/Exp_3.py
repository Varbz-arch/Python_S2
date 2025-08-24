#Find the greatest among two numbers. If numbers are equal than print 
# “numbers are equal”. 

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 > num2:
    print(f"The greatest number is {num1}.")
elif num2 > num1:
    print(f"The greatest number is {num2}.")
else:
    print("Numbers are equal.")
