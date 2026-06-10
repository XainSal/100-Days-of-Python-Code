import random
import os
import art

EASY = 10
HARD = 5

def set_difficulty(choice):
    if choice == "easy":
        return EASY
    elif choice == "hard":
        return HARD
    else:
        print("Invalid choice. Defaulting to easy.")
        return EASY

def check_guess(guess, answer):
    perc = (guess / answer) * 100
    if perc > 100:
        perc /= 10

    if guess < answer:
        if perc >= 50:
            print("Low")
            print("Guess again")
            return False # wrong guess
        else:
            print("Too low")
            print("Guess again")
            return False # wrong guess

    elif guess > answer:
        if perc <= 50:
            print("High")
            print("Guess again")
            return False # wrong guess
        else:
            print("Too high")
            print("Guess again")
            return False # wrong guess

    else:
        print(f"You got it! The answer was {answer}")
        return True # correct guess

def guess_number(difficulty):
    randomized_number = random.randint(1, 100)
    #print(randomized_number) # only for debugging
    lives = difficulty

    for attempts in range(difficulty):
        print(f"You have {lives} attempts remaining to guess the number")
        guess = int(input("Make a guess: "))
        result = check_guess(guess=guess, answer=randomized_number)

        if result:
            break
        else:
            lives -= 1

    if lives < 1:
        print(f"You have {lives} attempts remaining. You lose. The answer was {randomized_number}")

run_game = True

while run_game:
    os.system('cls||clear')
    print(art.logo)
    print("Welcome to the Number guessing game!")
    print("I'm thinking of a number between 1 and 100, try to guess it")
    get_difficulty = input("Type 'easy' or 'hard': ").lower()
    difficulty_mode = set_difficulty(get_difficulty)
    guess_number(difficulty_mode)

    if input("\nType 'y' to run again or 'n' to close: ").lower() == "n":
        run_game = False