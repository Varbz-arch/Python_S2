#Scan n values in range 0-3 and print the number of times each value has occurred. 

N = int(input("How many numbers? "))
numbers = []
for i in range(N):
    while True: 
        num = int(input(f"Enter (0-3) number {i+1}: "))
        if 0 <= num <= 3: 
            numbers.append(num)
            break  
        else:
            print("Oops! Invalid input! Please enter a number between 0 and 3.")
count_0 = numbers.count(0)
count_1 = numbers.count(1)
count_2 = numbers.count(2)
count_3 = numbers.count(3)
print("Number of 0's:", count_0)
print("Number of 1's:", count_1)
print("Number of 2's:", count_2)
print("Number of 3's:", count_3)
