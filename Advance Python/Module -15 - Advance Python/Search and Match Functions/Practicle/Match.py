import re

s = "Hello, World!"
print("Text Is : ",s)

match = re.match("Hello", s)

if match:
    print("Pattern found!")
else:
    print("Pattern not found.")