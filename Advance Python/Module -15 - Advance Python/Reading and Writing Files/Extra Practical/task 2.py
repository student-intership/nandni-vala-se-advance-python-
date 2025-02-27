# Open the file in read mode
with open("output.txt", "r") as file:
    # Read the file content
    data = file.read()
    
    # Print the content
    print(data)