#Create 2 sets s1 and s2 of n fruits each by taking input from user and find: 

set_1=set()
set_2=set()
for i in range(4):
    set_1.add(input("Enter the fruits 1: "))
for i in range(4):
    set_2.add(input("Enter the fruits 2: "))
print("Intersection: ", set_1.intersection(set_2))
print("Difference: ", set_1.difference(set_2))
print("Difference: ", len(set_1.union(set_2)))
print("Symmetric Difference: ", set_1.symmetric_difference(set_2))
