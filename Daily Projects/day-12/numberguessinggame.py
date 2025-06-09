from random import randint
from art import logo

MAX_NUMBER = 100
COMPUTER_NUMBER = randint(1, MAX_NUMBER)
lives = 10

print(logo)
print("Welcome to the Number Guessing Game!")

print(f"I'm thinking of a number between 1 and {MAX_NUMBER}.")

def mode_manager(total_lives):
    mode_choice = input("Would you to play on the hard mode or easy mode?: ").lower()

    if mode_choice == "hard":
        total_lives -= 5
    else:
        print("Invalid input. Easy mode automatically selected.")

    print(f"Due to your choice you start with {total_lives} lives.")
    return total_lives


lives = mode_manager(lives)

while lives > 0:
    user_guess = int(input("What's your guess?: "))
    if user_guess == COMPUTER_NUMBER:
        print(f"You guessed the correct number. Good job")
        break
        
    lives -= 1
    if user_guess > COMPUTER_NUMBER:
        print(f"Your guess is too high.\nYou have {lives} lives left.")
    else:
        print(f"Your guess is too low.\nYou have {lives} lives left.")

if lives == 0:
    print("Thank you for playing! The correct number was ", COMPUTER_NUMBER)
