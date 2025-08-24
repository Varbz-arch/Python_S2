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
