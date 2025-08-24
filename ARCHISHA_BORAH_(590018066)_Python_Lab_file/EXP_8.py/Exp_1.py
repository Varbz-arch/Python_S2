# Add few names, one name in each row, in “name.txt file”. 

with open("name.txt", "w") as file:
    file.write("\n".join(["Alice", "Ethan", "Oliver", "Isla", "Uma", "Noah", "Emma", "Liam", "Sophia"]))
with open("name.txt", "r") as file:
    names = file.read() 

# a. Count the number of names
name_count = len(names)
print(f"Total number of names: {name_count}")

# b. Count names starting with a vowel
vowels = {"A", "E", "I", "O", "U"}
vowel_count = sum(1 for name in names if name[0].upper() in vowels)
print(f"Number of names starting with a vowel: {vowel_count}")

# c. Find the longest name
longest_name = max(names, key=len)
print(f"The longest name is: {longest_name}")
