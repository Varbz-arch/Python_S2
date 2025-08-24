#Armstrong number. 

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
