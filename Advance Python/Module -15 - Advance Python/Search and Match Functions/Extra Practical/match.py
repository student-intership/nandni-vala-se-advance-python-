import re

s = "Hello, welcome to the world of Python."

pattern = input("Enter the word to match at the beginning of the string: ")

match = re.match(rf'^{pattern}', s) 

if match:
    print(f"Pattern '{pattern}' found at the beginning of the string.")
else:
    print(f"Pattern '{pattern}' not found at the beginning of the string.")
