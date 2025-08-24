#1
## Write a program to count and display the number of capital letters in a given string.

string=input("Enter the string")
count=0
for char in string:
    if char.isupper():
        count+=1
print(f"Number of capital letters: {count}")

#2
## Count total number of vowels in a given string.

string = input("Enter a string: ")
count = 0
vowels = "AEIOUaeiou"
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")

#3
#Input a sentence and print words in separate lines. 

string = input("Enter the sentence: ")
print("Words in the sentence:")
for word in string.split():
    print(word)

#4
#WAP to enter a string and a substring. You have to print the number of times 
#that the substring occurs in the given string. String traversal will take place from 
#left to right, not from right to left.

String="ABCDCDC"
SubString="CDC"
count=0

for i in range(len(String)-len(SubString)+1):
    if ((String[i]==SubString[0]) and (String[i:i+len(SubString)]==SubString)):
        count+=1
print(f"Output: {count}")

#5
#Given a string containing both upper and lower case alphabets. Write a Python 
#program to count the number of occurrences of each alphabet (case 
#insensitive) and display the same. 

String="ARchishA"
Str=String.lower()
for char in set(Str):
    print(Str.count(char),char.upper())

#6
#Program to count number of unique words in a given sentence using sets. 
#Initialize an empty set to store unique words

string=input("Enter the sentence:")
list=string.split(' ')
set=set(list)
count=len(set)
print(f"Number of Unique Words:{count} ")

#7
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

#8
#Take two sets and apply various set operations on them : 
#S1 = {Red ,yellow, orange , blue } 
#S2 = {violet, blue , purple} 

S1 = {"Red", "Yellow", "Orange", "Blue"}
S2 = {"Violet", "Blue", "Purple"}
print("Intersection: ", set_1.intersection(set_2))
print("Difference: ", set_1.difference(set_2))
print("Difference: ", len(set_1.union(set_2)))
print("Symmetric Difference: ", set_1.symmetric_difference(set_2))