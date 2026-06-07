import random
import os
from art import logo

cards = ["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"]

def check_score (cards_list):
    """Take a list of cards and return the score calculated from the cards"""
    score = 0
    for x in range(len(cards_list)):
        if "Ace" == cards_list[x]:
            score += 11
        elif "Jack" == cards_list[x] or "Queen" == cards_list[x] or "King" == cards_list[x]:
            score += 10
        else:
            score += cards_list[x]
    if score > 21 and 11 in cards_list:
        score -= 10
    if score == 21 and len(cards_list) == 2:
        score = 0
    return score

def check_winner(score_user, score_computer):
    if score_user ==  score_computer:
        return ("\n-----------------------------\n Draw\n-----------------------------\n")
    elif score_computer == 0:
        return "\n-----------------------------\n Lose, Opponent has blackjack\n-----------------------------\n"
    elif score_user == 0:
        return "\n-----------------------------\n Win with a Blackjack\n-----------------------------\n"
    elif score_user > 21:
        return "\n-----------------------------\n You went over. You lose\n-----------------------------\n"
    elif score_computer > 21:
        return "\n-----------------------------\n Opponent went over. You win\n-----------------------------\n"
    elif score_user > score_computer:
        return "\n-----------------------------\n You win\n-----------------------------\n"
    else:
        return "\n-----------------------------\n You lose\n-----------------------------\n"

def play_game():
    user_cards = []
    computer_cards = []
    print(logo)
    is_game_over = False

    for _ in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

    while not is_game_over:
        user_score = check_score(user_cards)
        computer_score = check_score(computer_cards)

        print(f" Your Cards: {user_cards}, Current score: {user_score}")
        print(f" Computer first card: {computer_cards[0]}")

        if computer_score == 0 or user_score == 0 or user_score > 21:
            is_game_over = True
        else:
            if input("\nType 'y' to get another card, type 'n' to pass: ") == 'y':
                user_cards.append(random.choice(cards))
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(random.choice(cards))
        computer_score = check_score(computer_cards)

    print(f"\n Your final hand: {user_cards}, Final score: {user_score}")
    print(f" Computer final hand: {computer_cards}, Final score: {computer_score}")
    print(check_winner(user_score, computer_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls||clear')
    play_game()