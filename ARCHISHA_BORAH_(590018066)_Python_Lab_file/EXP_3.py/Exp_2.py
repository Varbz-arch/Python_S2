#Check whether a given number is multiple of five or not. 

number = int(input("Enter a number: "))
if number % 5 == 0:
    print(f"The number {number} is a multiple of five.")
else:
    print(f"The number {number} is not a multiple of five.")
