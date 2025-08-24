''' Write a Python program to solve (x+y)*(x+y) 
Test data : x = 4 , y = 3 
Expected output: 49 '''

x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
result = (x + y) * (x + y)
print(f"The result of (x + y) * (x + y) where x = {x} and y = {y} is: {result}")
