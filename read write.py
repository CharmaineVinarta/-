# reading file
# always starts with 'with', then open function
# Option 1 to open
with open("file_test", "r") as f:
    print(f.read())

# or another way, this will itirate the code, there will be spacing everyline
with open("file_test", "r") as f:
    for line in f:
        print(line)

# or another way, no line, add .rstrip()
with open("file_test", "r") as f:
    for line in f:
        print(line.rstrip("\n"))

# other option to open
# if file i snot in the same folder do this, but double the backslash
with open("C:\\Users\\cemvi\\PycharmProjects\\pythonProject\\file_test", "r") as f:
    for line in f:
        print(line.rstrip("\n"))


# Writing file
# writing a file, if re-writing the old content will be deleted
with open("new_file", "w") as f:
    f.write("Hello World")

# if want to add, use mode a as append
with open("new_file", "a") as f:
    f.write(" adding a new word, Hello World")
