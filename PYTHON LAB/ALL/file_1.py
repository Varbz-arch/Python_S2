#Write a program to reverse any string

string = input()
lst=[]
for i in range(len(string), 0, -1):
    lst.append(string[i-1])
print(''.join(lst))
