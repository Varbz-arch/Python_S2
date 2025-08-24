def read_file(filename):
        print(f"Oops! The file '{filename}' does not exist.")
        choice = input("Do you want to create it? (yes/no): ")
        if choice == 'yes':
            with open(filename, 'w') as file:
                new_content = input("Enter content for the new file:\n")
                file.write(new_content)
            print(f"File '{filename}' has been created and content added! ")
            with open(filename, 'r') as file:
                updated_content = file.read()
                print(updated_content)
        else:
            print("No file was created.")
filename = input("Enter the filename (e.g., name.txt): ")
read_file(filename)
