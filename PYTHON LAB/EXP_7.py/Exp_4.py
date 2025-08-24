#Write a recursive function to print Fibonacci series upto n terms.

def fibonacci(N):
    if (N==1 or N==2):
        return 1
    F1=1
    F2=1
    F=F1+F2
    F2=F
    return fibonacci(N-1)+fibonacci(N-2)
N=int(input("Enter the value to fibonacci it: "))
for i in range(1, N+1):
    print(fibonacci(i))