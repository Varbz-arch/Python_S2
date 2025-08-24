#Write a Python function to print 1 to n using recursion. (Note: Do not use loop) 

def print_natural(N):
    if N<1:
        return 
    print_natural(N-1)
    print(N)

N=int(input("Enter the value: "))
print_natural(N)
