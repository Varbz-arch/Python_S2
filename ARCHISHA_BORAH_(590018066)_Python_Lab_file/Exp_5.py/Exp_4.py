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