import random
def i_binary_search(lst, X):
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
lst=sorted([int(random.random()*(10**6)) for _ in range(10**6)])
X=int(input("Enter the number that you wanna search?  "))
num=i_binary_search(lst,X)
if num== -1:
    print("NOT FOUND")
else:
    print("Number is found at the position: ", num+1)