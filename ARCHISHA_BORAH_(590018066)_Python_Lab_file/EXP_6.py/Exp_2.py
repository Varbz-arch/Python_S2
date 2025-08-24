#Create a tuple to store n numeric values and find average of all values. 
 
N = int(input("How many numbers?  "))
numbers = []
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
T = tuple(numbers)
average = sum(T) / N
print("The numbers that  you entered:", T)
print("Average of all values:", average)