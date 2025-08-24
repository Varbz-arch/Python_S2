s = "hello"
print(s[::-1]) #to reverse a string

def is_prime(n):
    if n <= 1:
        print("ERROR")
        return False
    for i in range(2, int(n**0.5)+1):    #n**0.5 means square root
        if n % i == 0:
            print("Its not a prime")
            return False
    print("Yes! Its a prime")
    return True
n=int(input("Enter the number to check if its prime or not: "))
is_prime(n)