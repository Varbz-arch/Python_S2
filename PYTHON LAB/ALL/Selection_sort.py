import random
def selection_sort(lst):
    n = len(lst)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] > lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
lst = [random.randint(1, 100) for _ in range(20)]   
print("Unsorted list:", lst)
selection_sort(lst)
print("Sorted list:", lst)


