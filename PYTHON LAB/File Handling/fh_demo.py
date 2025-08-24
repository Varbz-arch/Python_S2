# with open("log.txt", "w") as file:   #with statement means automatically closes the file.
#safe file handling
#     file.write("Something happened again!\n")
# with open("log.txt", "ab") as file:
#     file.write(b"Something happened again!!\n")

# f=open("log.txt","a") #Writing Data to a File
# f.write("yo i called u again")
# f.close

# f = open('log.txt', 'r') #Reading Data from a file
# content = f.read()
# print(content)  #in terminal
# f.close()

# Mode | Meaning | Notes
# 'r' | Read | File must exist.
# 'w' | Write | Truncates file if it exists or creates new.
# 'a' | Append | Adds data at end of file.
# 'r+' | Read + Write | Doesn't truncate file.
# 'w+' | Write + Read | Truncates file, then allows reading.
# 'a+' | Append + Read | Read/write, always appends at end.
# 'b' | Binary mode | Example: 'rb', 'wb'.
# 't' | Text mode | Default mode. Example: 'rt'.
#'x'  | Exclusive | Creates a new file but fails if the file already exists.

# Function | Purpose
# open(file, mode) | Opens a file.
# file.read(size) | Reads entire file or size bytes.
# file.readline() | Reads one line.
# file.readlines() | Reads all lines into a list.
# file.write(string) | Writes a string to file.
# file.writelines(list) | Writes list of strings to file.
# file.close() | Closes the file.

# Method | Meaning
# file.seek(offset) | Move file pointer to specific position.
# file.tell() | Tells current file pointer position.
# file.flush() | Force write buffered content to disk.

# Function | Purpose
# os.getcwd() | Get current working directory.
# os.chdir(path) | Change current directory.
# os.listdir(path) | List files and folders.
# os.mkdir(path) | Make a new folder.
# os.makedirs(path) | Make nested folders.
# os.remove(file) | Delete a file.
# os.rmdir(folder) | Remove empty folder.
# os.path.exists(path) | Check if path exists.

# Example of Error: IndentationError
# # Example of Exception: ZeroDivisionError
# Error | Problem in code (syntax errors, indentation errors). Can't be caught.
# Exception | Runtime errors that can be caught and handled.

# try:
#     # risky code
# except SomeException:  like fileNotFoundError
#     # handling code
# else:
#     # runs if no exception
# finally:
    # always runs
# try | Code that may cause an exception.
# except | What to do if exception occurs.
# else | Run if no exception occurs.
# finally | Always run (for cleaning up).

#raise: manually throws an exception
# age = int(input("Enter your age: "))
# if age < 0:
#     raise ValueError("Age cannot be negative!")
# else:
#     print(f"Your age is {age}")

#assert: quickly check the condition if its true
# assert 2 + 2 == 4  # Nothing happens
# assert 2 + 2 == 5  # Raises AssertionError

# seek()
# Moves the file pointer to a specific position in the file.
# file = open("file.txt", "r")
# file.seek(10)  # Moves to the 10th byte

# tell()
# Returns the current position of the file pointer.
# file = open("file.txt", "r")
# position = file.tell()
# print(position)

# flush()
# Forces the file to be written to disk.
# file = open("file.txt", "w")
# file.write("This will be written.")
# file.flush()

# The os module allows you to work with directories and file paths.
# import os
# # Check if file exists
# os.path.exists("file.txt")
# # Create a directory
# os.mkdir("new_folder")
# # List all files in a directory
# os.listdir(".")

#  Applications of File Handling
# Storing user data (like usernames, passwords)
# Data logging (error logs, system logs)
# Configuration files (.ini, .cfg, .json)
# Saving analysis results (ML models, data files)
