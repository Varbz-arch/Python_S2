#prime number

number = int(input("Enter a number: "))
a=1
for i in range(2, number):
    if(number%i==0):
        a=0
        break
if(a==0):
    print(f"{number} is not a prime number")
else:
    print(f"{number} is a prime number")
