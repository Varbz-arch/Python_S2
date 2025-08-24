#1
#factorial

number = int(input("Enter a number: "))
fact = 1
for i in range(1, number + 1):
    fact *= i 
print(f'Factorial of {number} is: {fact}') 

#2
#armstrong

num=int(input("Enter a number:"))
sum_digits=0
temp=num
order=len(str(num))
while(temp>0):
    digit=temp%10
    sum_digits += digit**order
    temp//=10
if num==sum_digits:
    print("Armstrong number")
else:
    print("Not an armstrong number")


#3
#fibonacci series

number = int(input("Enter a number: "))
n1=0
n2=1
print("0\n1")
for i in range(number-1):
    num=n1+n2
    n1=n2
    n2=num
    print(num) 

#4
#prime

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

#5
#palindrome

number = int(input("Enter a number: "))
num=0
N=number
while number>0:
    NUM=number%10
    num=num*10+NUM
    number=number//10
if num==N:
    print(f"{N} is a Palindrome")
else:
    print(f"{N} is not a Palindrome")

#6
#print sum of digits

number = int(input("Enter a number: "))
a=0
while number>0:
    n1=number%10
    a=a+n1
    number=number//10
print(a) 

#7
#count and print number which are divisble by 5 or 7

sum=0
for i in range(1,101):
    if(i%5==0 or i%7==0):
        sum+=1
        print(i)

#8
#lower case to upper case

string=str(input("Enter the string"))
result=""
for char in string:
    if 'a'<= char <='z':
        result+=chr(ord(char)-32)
    else:
        result+=char
print(f"Upper string: {result}")

#9
#primes between 1 to 100

for num in range(2, 101):
    prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            prime = False
            break
    if prime:
        print(num, end=" ")
print()

#10
#print a table of a number

number = int(input("Enter a number: "))
A=number
for i in range(1, 11):
    A=number*i
    print(A)

