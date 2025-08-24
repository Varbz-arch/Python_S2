def searching(file, word):
    with open(file, "r") as file:
        content = file.read()  
    if word in content:
        print(f"'{word}' is found in the file!")
    else:
        print(f"'{ word}' is NOT found in the file.")
file = input("Enter the file name: ")   
word = input("Enter the word: ")   

searching(file, word)