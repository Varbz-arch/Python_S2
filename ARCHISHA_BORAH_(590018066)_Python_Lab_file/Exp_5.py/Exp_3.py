#Input a sentence and print words in separate lines. 

string = input("Enter the sentence: ")
print("Words in the sentence:")
for word in string.split():
    print(word)
