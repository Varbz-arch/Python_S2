#Fibonacci series 

number = int(input("Enter a number: "))
n1=0
n2=1
print("0\n1")
for i in range(number-1):
    num=n1+n2
    n1=n2
    n2=num
    print(num)