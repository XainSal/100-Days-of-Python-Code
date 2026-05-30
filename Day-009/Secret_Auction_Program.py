import os
from art import logo

bidders_list = {}
other_bidders = "yes"

def find_highest_bidder(bidding_record):
    highest_bidder = 0
    winner = ""
    for bidder in bidding_record:
        if bidding_record[bidder] > highest_bidder:
            highest_bidder = bidding_record[bidder]
            winner = bidder
    print(f"The winner is: {winner} with a bid of ${highest_bidder}")

print(logo)
print("Welcome to the secret auction program.")

while other_bidders == "yes":
    name = input("What is Your Name: ")
    price = int(input("What's your bid?: "))
    bidders_list[name] = price
    other_bidders = input("Are there any bidders? Type 'yes' or 'no'\n").lower()
    if other_bidders == "no":
        find_highest_bidder(bidders_list)
    elif other_bidders == "yes":
        os.system('cls||clear')