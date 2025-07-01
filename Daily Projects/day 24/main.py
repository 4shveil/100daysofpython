# with open("/Users/Dell/Documents/python-stuff/day 24/my_file.txt") as file:
#     contents = file.read()

#     print(contents)
#     file.close()


with open("./day 24/my_file.txt", mode="w") as file:
    file.write("New text.")