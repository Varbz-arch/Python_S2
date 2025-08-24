#print sum of digits. 

number = int(input("Enter a number: "))
a=0
while number>0:
    n1=number%10
    a=a+n1
    number=number//10
print(a)
