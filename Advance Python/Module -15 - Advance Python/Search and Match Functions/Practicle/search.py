import re

t = "Hello, welcome to the world of Python."
print("Text Is : ",t)
pattern = input("Enter Word to search:")

result = re.search(pattern, t)

if result:
    print("Pattern found")
else:
    print("Pattern not found")