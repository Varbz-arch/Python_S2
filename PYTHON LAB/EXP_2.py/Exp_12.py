#Using membership operator find whether a given number is in sequence (10,20,56,78,89) 

sequence={10,20,56,78,89}
n=int(input("Enter the number to check whether the number is in sequence or not:"))
if n in sequence:
    print(f'{n} is in the sequence')
else:
    print(f'{n} is not in the sequence')
    

