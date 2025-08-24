#lower cases to upper case  

string=str(input("Enter the string: "))
result=""
for char in string:
    if 'a'<= char <='z':
        result+=chr(ord(char)-32)
    else:
        result+=char

print(f"Upper string: {result}")