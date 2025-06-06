from random import choice, shuffle

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Easy level - Solution

# TODO: Use len to find out how many letter, number and symbols are in each list
listPassword = []
easyPassword = ""
hardPassword = ""

# TODO: Generate the exact amount of letter symbols and numbers requested by the user through a for loop
for _ in range(nr_letters):
    listPassword += choice(letters)

for _ in range(nr_symbols):
    listPassword += choice(symbols)

for _ in range(nr_numbers):
    listPassword += choice(numbers)

for char in listPassword:
    easyPassword += char

print(f"Your weak password: {easyPassword}")

shuffle(listPassword)

for char in listPassword:
    hardPassword += char

print(f"Your strong password: {hardPassword}")
