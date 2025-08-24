# import random
def counting_sort(lst):
        count = [0] * (max(lst) + 1)
        for freq in lst:
            count[freq] += 1
        index = 0
        for i in range(len(count)):
            while count[i]>0:
                lst[index] = i
                index += 1
                count[i]-=1
lst=[2,0,5,2,3]
# lst= [random.randint(1, 10) for _ in range(5)]
# print("Random numbers:", lst)
counting_sort(lst)
print("Sorted list:", lst)
