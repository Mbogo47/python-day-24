with open("c:/Users/USER/Desktop/my_file.txt") as file:
    h = file.read()
    a = int(h)
    print(a)
    print(type(a))

# w - write replaces everything
with open("my_file.txt", mode ="w") as file:
    file.write("new text")

# a - append - adds to the text already there
with open("my_file.txt", mode ="a") as file:
    file.write("\nnew text")

# If file being opened doesn't exist it will be created and only works on write mode
with open("new_file.txt", mode ="w") as file:
    file.write("\nnew text")

