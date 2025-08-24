# converts decimal to octal,binary,and hexadecimal

num=int(input("Enter any number: "))
binary=bin(num)[2:]
octal=oct(num)[2:]
hexadecimal=hex(num)[2:]
print(f"Binary of {num} is {binary}")
print(f"Octal of {num} is {octal}")
print(f"Hexadecimal of {num} is {hexadecimal}")