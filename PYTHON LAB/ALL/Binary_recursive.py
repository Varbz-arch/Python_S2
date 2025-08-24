import random

def r_binary_search(lst,n,start,end):
    if start <= end:
        mid = (start+end)//2
        if(n == lst[mid]):
            return mid
        elif n < lst[mid]:
            return r_binary_search(lst,n,start,mid-1)
        else:
            return r_binary_search(lst,n,mid+1,end)
            
    return -1

lst=sorted([int(random.random()*(10**6)) for _ in range(10**6)])
X=9554

num=r_binary_search(lst,X, 0, len(lst))

if num== -1:
    print("NOT FOUND")
else:
    print("Number is found at the position: ", num+1)