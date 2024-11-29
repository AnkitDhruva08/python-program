# Opening a file in write mode
file = open("example.txt", "w")

file.write("Hello, world!\n")
file.write("This is a second line.")

# Always close the file to save changes
file.close()
