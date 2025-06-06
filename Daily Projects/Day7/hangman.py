import random
import hangman_words
from hangman_art import stages, logo

word_list = hangman_words.word_list

lives = 6

print(logo)

chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []
guessed_letters = []

while not game_over:

    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    print(f"Previously guessed letters: {guessed_letters}".format(guessed_letters=guessed_letters))
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You have already guessed that letter. Please try again.")
        continue

    guessed_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1

        print(f"You guessed {guess} which is not in the word. You just lost a life, you have {lives} lives remaining.")

        if lives == 0:
            game_over = True

            print(f"***********************YOU LOSE**********************\nThe word was: {chosen_word}. Thank you for playing!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(stages[lives])
