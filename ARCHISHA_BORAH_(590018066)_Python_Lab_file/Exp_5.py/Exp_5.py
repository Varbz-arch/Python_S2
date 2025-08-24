#Given a string containing both upper and lower case alphabets. Write a Python 
#program to count the number of occurrences of each alphabet (case 
#insensitive) and display the same. 

String="ARchishA"
Str=String.lower()
for char in set(Str):
    print(Str.count(char),char.upper())