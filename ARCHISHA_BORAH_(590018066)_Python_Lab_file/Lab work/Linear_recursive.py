def linear_search(l1,n):
    for i in range(len(l1)):
        if(n == lst[i]):
            return i
    return -1

import random
n = int(input("Enter a number:"))
lst = sorted(int(random.random()*10**6) for i in range(10**6))
search = linear_search(lst,n)
print(search)