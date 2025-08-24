#bubble sort, selection sort, insertion sort, merge sort, quick sort
#input: unsorted sequence
#output: sorted sequence

N=[3,1,2,4,5]
import random
N = [int(random.random() * (10**2)) for _ in range(20)]
print("Random list:")
print (N)
# N=[3,1,2,4,5]
n=len(N)
for i in range(n):
    # if (N==N2):
        # print(i)
        # break
    for j in range(n-i-1): 
        if N[j] > N[j + 1]:
            temp=N[j]
            N[j]=N[j+1]
            N[j+1] = temp 
print("Sorted:")
print(N)
 

# def is_sorted(lst):
#     return lst==sorted(lst)
# lst=[1,2,3,4]
# print(is_sorted(lst))
# lst=[3,2,4,5]
# print(is_sorted(lst))

# import random
# N = [int(random.random() * (10**2)) for _ in range(20)]
# print("Random list:")
# print(N)
# n=len(N)
# for i in range(n-1):
#     for j in range(i+1, n):
#         if N[i] > N[j]:
#             temp=N[i]
#             N[i]=N[j]
#             N[j] = temp 
# print("Sorted:")
# print(N)