import random
import os
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.words_list).lower()

keep_going = True
lives = 6
already_guessed = []

print(hangman_art.hangman_header)

#Testing Code
#print(f"The Chosen Word is: {chosen_word}")

#Creating blanks
display = []
for number in range(0, len(chosen_word)):
    display.append("_")

while keep_going:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1:
        print("Only a single letter is allowed.\n")
        continue
    elif not guess.isalpha():
        print("Only letters are allowed.\n")
        continue
    elif guess in display or guess in already_guessed:
        print(f"You've already guessed the letter '{guess}'.\n")
        continue

    os.system('cls||clear')

    for number in range(0, len(chosen_word)):
        if chosen_word[number] == guess:
            display[number] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"The letter '{guess}' is not in the word. You lose a life.")

    print(f"{' '.join(display)}\n")
    print(hangman_art.hangman_ascii_art[lives])
    print("")

    if "_" not in display:
        print("You Won!")
        keep_going = False
    elif lives < 1:
        print(f"You Lose. The word was: {chosen_word}")
        keep_going = False

    already_guessed.append(guess)