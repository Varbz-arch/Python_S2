# Write a program to count and display the number of capital letters in a given string. 

string = input("Enter a string: ")
count = 0
for char in string:
    if char.isupper():    #isupper: for uppercase #islower: for lowercase
        count += 1
print(f"Number of capital letters: {count}")
