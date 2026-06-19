import random
import os
from game_data import data
from art import logo, vs


def select_random_persons(person1):
    person2 = random.choice(data)
    while person1['name'] == person2['name']:
        person2 = random.choice(data)
    return person2

def compare_score(com_a,com_b):
        if com_a["follower_count"] > com_b["follower_count"]:
            return "A"
        elif com_b["follower_count"] > com_a["follower_count"] :
            return "B"
        else:
            return "D"

def check_winner(choice, result, score):
    if result == "D":
        print("both player have same number of followers")
        return score
    elif choice == result:
        score += 1
        print(f"You're right!")
        return score
    else:
        print(f"\nSorry, That's Wrong. Final score: {score}")
        score = 0
        return score

def game():
    total_score = 0
    end_game = False
    competitor_a = random.choice(data)
    winning = False
    while end_game != True:
        os.system('cls||clear')
        print(logo)
        if winning:
            print(f"You're right!, Current Score: {total_score}")
        else:
            print(f"Current Score: {total_score}")
        competitor_b = select_random_persons(competitor_a)
        print(f"Compare A: {competitor_a['name']}, {competitor_a['description']}, from {competitor_a['country']}")
        print(vs)
        print(f"Against B: {competitor_b['name']}, {competitor_b['description']}, from {competitor_b['country']}")
        user_choice = input("\nWho has more followers? Type 'A' or 'B': ").upper()
        win = compare_score(competitor_a,competitor_b)
        total_score = check_winner(choice=user_choice, result=win, score=total_score)
        if win == "B" or win == "D" and total_score > 0:
            competitor_a = competitor_b
            winning = True
        elif win == "A" and total_score > 0:
            winning = True
        if total_score < 1:
            continue_game = input("\nDo you want to play the game again. type 'y' for yes and 'n' for no: ").lower()
            if continue_game == 'n':
                end_game = True
            os.system('cls||clear')

game()