import random
# N = random.sample(range(10), 5)
N = [int(random.random() * (10)) for _ in range(10)]
print("Random list:")
print(N)
n=len(N)
for i in range(1,n):
    num=N[i]
    j = i

    # while j >= 0 and N[j] >= num:  
    #     N[j + 1] = N[j]
    #     j-=1
    #     print(j)
    # N[j+1] = num
    
    
    
    # If i initialise then what will happen
    while j > 0 and N[j - 1] > num:  
        N[j] = N[j - 1]   # Shift the larger element to the right
        j -= 1  # Move the index left
        print(j)
        N[j] = num  # Insert the element in the correct position
print("Sorted array:", N)       
        
        
#         if num < N[j-1]:
#             N[i], N[i-1] = N[i-1], N[i]
# print("Sorted array:", N)
# for i in range(1, len(N)):  # Start from the second element
#     key = N[i]
#     j = i - 1
    
#     # Shift elements that are greater than key
#     while j >= 0 and N[j] > key:
#         N[j + 1] = N[j]
#         j -= 1
    
#     # Insert key at its correct position
#     N[j + 1] = key

# print("Sorted array:", N)
