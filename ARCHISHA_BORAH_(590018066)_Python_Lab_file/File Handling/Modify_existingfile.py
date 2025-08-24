def read_file(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print(f"Yes! The file '{filename}' exists. \nHere's its content:\n")
            print(content)
        choice = input("\nDo you want to (a)ppend or (e)mpty the file?: ")
        if choice == 'a':
            with open(filename, 'a') as file:  
                new_content = input("Enter content to append:\n")
                file.write("\n" + new_content)  
            print(f"Content appended to '{filename}' successfully!")
            with open(filename, 'r') as file:
                updated_content = file.read()
                print(updated_content)
        elif choice == 'e':
            with open(filename, 'w') as file:  
                new_content = input("File emptied! Enter the content: \n")
                file.write(new_content)
            print(f"'{filename}' has been emptied and new content added!")

        else:
            print("Invalid choice. No changes made.")
filename = input("Enter the filename (e.g., name.txt): ")
read_file(filename)
