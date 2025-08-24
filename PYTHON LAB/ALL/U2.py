# Hashable
# x = (1, 2, 3)
# print(hash(x))  # Works
# Not hashable
# y = [1, 2, 3]
# print(hash(y))  #TypeError: unhashable type: 'list'

# Examples of hashable objects:
# int
# float
# str
# tuple (only if all its elements are hashable)
# Examples of non-hashable objects:
# list
# dict
# set

# def normal_function():
#     return [1, 2, 3]

# print(normal_function())  # Output: [1, 2, 3]
# def generator_function():
#     yield 1
#     yield 2
#     yield 3

# gen = generator_function()
# print(next(gen))  # Output: 1
# print(next(gen))  # Output: 2
# print(next(gen))  # Output: 3

# #STRIP()
# text = "   Hello World!   \n"
# print(text.strip()) 
# #SPLIT()
# text = "Hello        World   Python"
# cleaned = " ".join(text.split())
# print(cleaned)  

# s = "hello world"
# print(s[0], s[1:5])      # Indexing, Slicing
# print(s.split())         # split()
# print(s.upper())         # String function

# lst = [1, 2, 3]
# lst.append(4)            # List method
# print(lst)
# print(lst[1:3])          # Slicing
# lst2 = [x*2 for x in lst] # List comprehension
# print(lst2)
# lst3=lst*2
# print(lst3)
# nested_lst = [[1,2], [3,4]] # Nesting
# print(nested_lst)

# t = (1, 2, 3)
# print(t.index(2))  #elements wise      # Tuple method
# print(t[1])  #index wise
# nested_t = ((1,2), (3,4)) # Nesting
# print(nested_t)

# s = {1, 2, 3}
# s.add(4)                 # Set method
# print(s)
# print(s.union({5,6}))    # Set operation

# d = {"a": 1, "b": 2}
# print(d.get("a"))         # to retrieve the value for the key "a"
# print(d.keys())           #to get a list of keys in the dictionary
# print(d.items())          #to get a list of key-value pairs (tuples)
# print(d.get("c", "Key not found"))  
# d = {
#     "person1": {"name": "Alice", "age": 25},
#     "person2": {"name": "Bob", "age": 30}
# }
# print(d["person1"]["name"])  
# print(d["person2"]["age"])   


# print(sorted([3,1,2]))    # Sorting
# print(list((1,2,3)))      # Typecasting tuple to list

# def greet(name="Guest"):  # Default argument
#     """Says hello"""      # Documentation
#     return "Hello " + name
# print(greet("Alice"))
# #docstring. It is a string that provides information 
# # about the function, explaining what the function does.
# #  It is placed immediately after the function definition.
# print(greet.__doc__)


# def add(*args):
#     return sum(args)
# print(add(1,2,3))

# x = 10
# def f():
#     global x
#     x = 20
# f()
# print(x) 

# def total(lst):  #Passing Collections to Functions
#     return sum(lst)
# print(total([1,2,3]))

# def apply(func, val): #Passing Functions to Functions
#     return func(val)
# print(apply(lambda x: x*2, 4))

# def fact(n):  #RECURSION
#     if n == 0: return 1
#     return n * fact(n-1)
# print(fact(5))

# nums = [1,2,3,4,5]
# # print(list(map(lambda x: x*x, nums)))    # map
# print(list(filter(lambda x: x%2==0, nums))) # filter
# usually 0 is considered as false in bool
# but in the above case its, x%2 is the remainder that they r talking about
# def outer():
#     def inner():
#         return "Inside inner"
#     return inner()
# print(outer())

# def change_list(lst):
#     lst.append(100)
# def change_num(num):
#     num += 10
# mylist = [1,2,3]
# mynum = 5
# change_list(mylist)
# change_num(mynum)
# print(mylist)  # Changed [1,2,3,100]
# print(mynum)   # Not changed 5
