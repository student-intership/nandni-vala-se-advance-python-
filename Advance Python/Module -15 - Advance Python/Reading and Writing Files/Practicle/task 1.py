# Open the file in read mode
with open("output.txt", "r") as file:
    # Read the contents of the file
    contents = file.read()
    
    # Print the contents
    print(contents)