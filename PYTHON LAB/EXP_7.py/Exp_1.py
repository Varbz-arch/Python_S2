#Write a Python function to find the maximum and minimum numbers from a sequence of numbers.  (Note: Do not use built-in functions.) 

def min(lst):  
    min_value = lst[0]  
    for i in range(len(lst)):  
        if lst[i] < min_value:
            min_value = lst[i]  
    return min_value  
def max(lst):  
    max_value = lst[0]  
    for i in range(len(lst)):  
        if lst[i] > max_value:
            max_value = lst[i]  
    return max_value  
list_1 = []  
N = int(input("How many numbers? "))  
for i in range(N):
    a = int(input("Data: "))  
    list_1.append(a)  

print(list_1)  

print(f"Minimum value is: {min(list_1)}") 
print(f"Maximum value is: {max(list_1)}") 

