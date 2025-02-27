filename = "simple.txt"

with open(filename, "w") as file:
    file.write("This is a sample string written into the file.\n")
    file.write("Python makes file handling easy!")

print(f"File '{filename}' created and string written successfully.")
