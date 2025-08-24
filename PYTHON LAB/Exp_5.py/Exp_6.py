#Program to count number of unique words in a given sentence using sets. 
#Initialize an empty set to store unique words

string=input("Enter the sentence:")
list1=string.split(' ')
set1=set(list1)
count=len(set1)
print(f"Number of Unique Words:{count} ")