# Write a program to find left shift and right shift values of a given number. 

n = int(input("Enter a number: "))
shift = int(input("Enter the number of positions to shift: "))
left_result = n << shift
right_result = n >> shift
print(f"The result of left shift {n} by {shift} positions is: {left_result}")
print(f"The result of right shift {n} by {shift} positions is: {right_result}")