# In Python, a for or while loop's else block executes only if the loop completes all iterations without a break.
# print (__name__)
    # task_name = input("Enter task: ")
    # due_date = input("Enter due date (DD-MM-YYYY): ")
    # tasks.append({"task": task_name, "completed": False, "due_date": due_date})

            # due_date=task.get("due_date", "No due date")  
# age = 20
# print("AGE IS " + str(age) )

# def main():
#     print("Hello world! Imma print the numbers from 1 to 10")
#     for i in range(1,11):
#         print(i)
#     for j in range(1,11,3): # how much to jump by each time
#         print(j)
# if __name__=='__main__':
#     main()

# from Modules import mymodule1

# # Python code to test that 
# # tuples are immutable 
# tuple1 = (0, 1, 2, 3) 
# # tuple1[0] = 4
# # print(tuple1) 

# # Python code to test that 
# # strings are immutable 
# message = "Welcome to GeeksforGeeks"
# # message[0] = 'p'
# # print(message)

# # Python code to test that 
# # lists are mutable 
# my_list = [1, 2, 3]
# my_list.append(4)
# print(my_list) 
# my_list.insert(1,5)
# print(my_list) 
# my_list.remove(2)
# print(my_list) 
# popped_element = my_list.pop(0)  #last updated my_list is being popped
# print(my_list)         
# print(popped_element)  

# # Python code to test that 
# # dictionarys are mutable 
# my_dict = {"name": "Ram", "age": 25}
# new_dict = my_dict
# new_dict["age"] = 37
# print(my_dict)   
# print(new_dict)

# #even sets too
# my_set = {1, 2, 3}
# new_set = my_set
# new_set.add(4)
# print(my_set)    
# print(new_set) 

# if 5 > 2:
#     print("Five is greater than two")  # Indented properly

# s = "Hello World"
# print(s.lower())  
# print(s.upper())
# print(s.replace("World", "Python"))  

# name = "Alice"
# print(f"Hello, {name}")
# #or
# print("Hello, {}".format(name))

# a = "Hello "
# b = "Python"
# print(a + b)      # Concatenation
# print(a * 3)      # Repetition
# print("Hell" in a) # Membership
# print("Py" not in b)

# a = 10          # int
# b = 5.5         # float
# c = 1 + 2j      # complex

# name = str(input("Enter your name: "))
# print("Hello", name)

# #XXXXXX
# student_name = "John"    # variable
# MAX_SPEED = 120          # constant
# class Car:               # class
#     pass

# x=5
# x+=9
# print(x is 8)  #identity
# print(x is not 8)

# x = 6
# print(type(x))  # <class 'int'>
# print(id(x))    # Memory address

# if, elif, else
# x = 10
# if x > 0:
#     print("Positive")
# elif x == 0:
#     print("Zero")
# else:
#     print("Negative")
# # nested if
# x=10
# if x > 0:
#     if x < 100:
#         print("x is a positive number less than 100")
# match statement (Python 3.10+)
# value = 4  
# match value: #match is to match as its in built keywords
#     case 1:
#         print("One")
#     case 2:
#         print("Two")
#     case _:
#         print("Other")

# while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# # for loop
# for i in [1, 2, 3]:
#     print(i)

# for i in range(1,5):
#     if i == 3:  # 3 reached? STOP
#         break
#     print(i)
# for i in range(5):
#     if i == 2:  # 2 skipped
#         continue
#     print(i)
# def dummy():
#     pass  # Placeholder for future code

# for i in range(3):
#     print(i)
# else:
#     print("Loop finished!")  
    #After the for loop finishes normally (without break),
    # the else block also runs.

#nested loops
# for i in range(2):
#     for j in range(3):
#         print(i, j)

