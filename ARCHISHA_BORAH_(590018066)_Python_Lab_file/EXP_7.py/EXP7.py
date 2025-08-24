#1
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



#2
#Write a Python function that takes a positive integer and returns the sum of the cube of all the positive integers smaller than the specified number. 

def sum_of_cubes(n):
    total = 0
    for i in range(1, n+1):
        total += i ** 3
    return total

n = int(input("Enter a number: "))
print("Sum of cubes: ", sum_of_cubes(n))
print()


#3
def print_natural(N):
    if N<1:
        return 
    print_natural(N-1)
    print(N)

N=int(input("Enter the value: "))
print_natural(N)

#4
def fibonacci(N):
    if (N==1 or N==2):
        return 1
    F1=1
    F2=1
    F=F1+F2
    F2=F
    return fibonacci(N-1)+fibonacci(N-2)
N=int(input("Enter the value to fibonacci it: "))
for i in range(1, N+1):
    print(fibonacci(i))

#5
volume_cone=lambda r,h: (1/3) * 3.14 * r**2 * h
r=int(input("Enter the radius of the cone: "))
h=int(input("Enter the height of the cone: "))
print(volume_cone(r,h))


#6
# Write a lambda function which gives tuple of max and min from a list.

find_max = lambda lst: (max(lst))
find_min = lambda lst: (min(lst))
print(find_max([10, 6, 8, 90, 12, 56]),find_min([10, 6, 8, 90, 12, 56])) 

#7
#Write functions to explain mentioned concepts: 

#a. Keyword argument 

def sum(x, y=4):
    return x+y
answer=sum(4)
print("Answer is: ", answer)

#b. default agrument

def sum(*args):
    total=0
    for i in args:
        total+=i
    return total
answer=sum(1,2,3,4)
print(answer)

#c. Variable length argument 

def sum(**kargs):
    total=0
    for key in kargs.keys():
        total+=kargs[key]
    return total
SUM=sum(x=1,y=2,z=3)
print(SUM)
