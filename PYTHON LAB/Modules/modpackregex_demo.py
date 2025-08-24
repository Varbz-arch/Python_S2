# #modules is a file containing python definations and statements
# math.ceil: higher round off
# math.floor: lower rounf off
# Package: A directory (folder) that contains multiple Python modules and a special __init__.py file.
#basically its a collection of modules
# # Packages allow you to organize your modules hierarchically.

# BUILT-IN MODULES
# sys, math, time, os->Provides functions for interacting with the operating system 
#                         (e.g., file handling, directories).
import sys
print("list of command line args: ", sys.argv)  # List of command-line arguments
import math
print(math.sqrt(16))  # Output: 4.0
import time
print(time.time())  # Current time in seconds since the epoch
import os
print(os.getcwd())  # Current working directory

# regex
# re.match(): Matches a pattern at the beginning of the string.
# re.search(): Searches for the first occurrence of the pattern in the string.
#  only finds the first match in the string — not all matches.
# re.sub(): Replaces occurrences of a pattern in a string with a replacement.
# re.findall(): Returns all matches of a pattern in a string as a list.
# re.finditer(): Returns an iterator yielding match objects for all occurrences.

import re
result = re.match(r"\d+", "123abc")
if result:
    print(result.group())  # Output: 123

result = re.search(r"\d+", "abc123xyz44")
if result:
    print(result.group())  # Output: 123

result = re.sub(r"\d", "#", "abc123xyz")
print(result)  # Output: abc###xyz

result = re.findall(r"\d+", "22abc123xyz456")
print(result)  # Output: ['22', '123', '456']

result = re.finditer(r"\d+", "abc123xyz456")
for match in result:
    print(match.group())  # Output: 123 456
#  result → Match object (full info)
#  result.group() → Just the matched text

# meta characters....  special characters used in regex patterns:
# .: Matches any character except a newline.
# ^: Matches the beginning of a string.
# $: Matches the end of a string.
# []: Matches any one of the characters inside the square brackets.
# |: Acts as an OR operator.
# *: Matches zero or more of the preceding element.
# # +: Matches one or more of the preceding element.

# character classes....allow you to match specific types of characters:
# \d: Matches any digit (equivalent to [0-9]).
# \w: Matches any word character (letters, digits, and underscore).
# Word character (a-z, A-Z, 0-9, _)
# \s: Matches any whitespace character.
# \D, \W, \S: Match non-digit, non-word, and non-whitespace characters, respectively.

# () is to define the groups and allows you to extract specific parts of the matched string.

import re
text = "cat bat cow rat mat llama venom"
result = re.findall(r".at", text)
print(result)

text = "yo hello world"
result = re.match(r"^yo", text)
print(result.group())  #^hello matches "hello" only if it's at the start.

text = "welcome to my world"
result = re.search(r"world$", text)
print(result.group())

text = "abbbbbc"
result = re.search(r"ab*c", text)
print(result.group())  #b* means "zero or more b's" between 'a' and 'c'.

text = "ac abc abbc abbbc"
result = re.findall(r"ab+c", text)
print(result)   #b+ means "one or more b's".

text = "cat bat mat rat fat"
result = re.findall(r"[cb]at", text)
print(result)

text1= "Phone:  123-456-7890"
text2 = "Phone:\n123\t-456-7890"
# Find all digits
digits = re.findall(r"\d", text1)
print(digits)
# Find all words
words = re.findall(r"\w+", text1)
print(words)
# Find all spaces
spaces1 = re.findall(r"\s", text1)
spaces2 = re.findall(r"\s", text2)
print(spaces1)
print(spaces2)


