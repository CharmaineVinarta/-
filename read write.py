# always starts with 'with', then open function

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

  
# if file i snot in the same folder do this, but double the backslash
with open("C:\\Users\\cemvi\\PycharmProjects\\pythonProject\\file_test", "r") as f:
    for line in f:
        print(line.rstrip("\n"))
