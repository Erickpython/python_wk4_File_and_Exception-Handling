# Create a program that reads a file and writes a modified version to a new file

with open("firstfile.txt", "w") as file:
    file.write ("1. I love python programming.\n2. I enjoy learning new technologies.\n")
    

# Ask the user for a filename and handle errors if it doesn’t exist or can’t be read

filename = input("Enter the filename to read: ")   #filename= "firstfile.txt"

try:
    with open(filename, "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    print("Error: The file does not exist.")