from art import logo
print (logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(direction_caesar, original_text, shift_amount):
    caesar_text = ""

    if direction_caesar == 'decode':
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            caesar_text += letter
            continue

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        caesar_text += alphabet[shifted_position]
        
    print(f"Here is the encoded result: {caesar_text}")

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(direction_caesar=direction, original_text=text, shift_amount=shift)

    if input("Type 'yes' if you want to go again. Otherwise type 'no'? ") == "no":
        break
