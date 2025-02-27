import re

t = ("Nature holds an unparalleled ability to rejuvenate, inspire, "
      "and calm the human spirit. When we immerse ourselves in nature—whether it's walking through a forest," 
      "listening to the waves on a beach, or gazing at a mountain range—we feel a deep connection to"
      "the world around us. Nature’s beauty, in its simplest form," 
      "has the power to soothe our minds, reduce stress, and enhance our overall well-being.")
print("Text Is : ",t)
pattern = input("Enter Word to search:")

result = re.search(pattern, t)

if result:
    print("Pattern found")
else:
    print("Pattern not found")