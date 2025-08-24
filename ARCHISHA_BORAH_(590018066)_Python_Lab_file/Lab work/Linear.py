'''def get_binary(N):
    rep=[]
    while(N!=0):
        rep.append(N%2)
        N=N//2
    return ''.join(rep.reverse())
N = int(input("Please enter a number:"))
get_binary(N) '''

'''def i_binary_search(lst, X, start, end):
    start=0
    end=len(lst)-1
    while start<=end:
        mid=(end+start)//2
        if X==lst[mid]:
            return mid
        elif X<lst[mid]:
            start=mid+1
        else:
            end=mid-1
    return -1
lst=[1,2,3,4,5,6,7,8,9,10]
X=7
num= i_binary_search(lst, X, 0, len(lst)-1)
print(num)'''
#running time: big oh(n)
    


'''def i_binary_search(lst, X, start, end):
    while start <= end:
        mid = (start + end) // 2
        if lst[mid] == X:
            return mid 
        elif lst[mid] < X:
            start = mid + 1
        else:
            end = mid - 1  
            
    return -1 
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
X = 3
print(i_binary_search(lst, X, 0, len(lst) - 1)) '''

import random
def linear_search(lst, X):
    for i in range(len(lst)):
        if lst[i]==X:
            return i
    return -1
lst=[int(random.random()*(10**6)) for _ in range(10**6)]
X=int(input("Enter the number that you wanna search?  "))
num=linear_search(lst,X)
if num== -1:
    print("NOT FOUND")
else:
    print("Number is found at the position: ", num+1)

    
'''num=int(input("Enter the number to search:  "))
lst.sort()
print(lst)
search=linear_search(lst, num)
print(search)   '''