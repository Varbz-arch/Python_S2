def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("Yes! The file does exitst and the content of it:\n", content)
    except FileNotFoundError:
        print("File does not exist.")
filename = input("Enter the filename (e.g., name.txt): ")
read_file(filename)

