#Print the table of a number:  


number = int(input("Enter a number: "))
A=number
for i in range(1, 11):
    A=number*i
    print(f"{number}*{i}={A}")