#Write a program to find common elements from the two lists

lst1 = [1,2,3,4,6,8]
lst2 = [2,4,6,8,10]
common_elements = list(set(lst1) & set(lst2))
if common_elements:
    print("Common elements:", common_elements)
else:
    print("No common elements found.")
