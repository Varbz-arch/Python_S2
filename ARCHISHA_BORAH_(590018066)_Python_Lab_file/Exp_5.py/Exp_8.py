#Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple} 


set_1 = {"Red", "Yellow", "Orange", "Blue"}
set_2 = {"Violet", "Blue", "Purple"}

print("Intersection: ", set_1.intersection(set_2))
print("Difference: ", set_1.difference(set_2))
print("Difference: ", len(set_1.union(set_2)))
print("Symmetric Difference: ", set_1.symmetric_difference(set_2))

