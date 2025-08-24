#Store integers in a file. 

with open("numbers.txt", "w") as file:
    file.write("\n".join(map(str, [45, 123, 67, 150, 200, 89, 301, 78, 99, 500])))
with open("numbers.txt", "r") as file:
    numbers = [int(line.strip()) for line in file.readlines()]

# a. Find the max number
max_num = max(numbers)
print(f"The maximum number is: {max_num}")

# b. Find the average of all numbers
average = sum(numbers) / len(numbers)
print(f"The average of all numbers is: {average:.2f}")

# c. Count numbers greater than 100
count_gt_100 = sum(1 for num in numbers if num > 100)
gt_100 = [num for num in numbers if num > 100]
print(f"Count of numbers greater than 100: {count_gt_100}") #this is to print the numbers 
print(f"Numbers greater than 100: {gt_100}")
