# Count total number of vowels in a given string.

string = input("Enter a string: ")
count = 0
vowels = "AEIOUaeiou"
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")
