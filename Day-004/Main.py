# We import random so the computer (NPC) can make a random choice
import random

# Ask the user to choose Rock, Paper, or Scissors
# 0 = Rock, 1 = Paper, 2 = Scissors
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors: "))

# The computer randomly chooses a number between 0 and 2
npc_choice = random.randint(0,2)

# This list stores the names of choices in correct order
rps_list = ['Rock', 'Paper', 'Scissors']

# This list stores ASCII art for each choice (visual representation)
rps = [
'''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''' # Rock
, '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''' # Paper
, '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' # Scissors
]

# Check if the user input is valid (must be 0, 1, or 2)
if user_choice == 0 or user_choice == 1 or user_choice == 2:
    # If both choices are the same → draw
    if user_choice == npc_choice:
        print(f"You Chose {rps_list[user_choice]}: {rps[user_choice]}")
        print(f"NPC Chose {rps_list[npc_choice]}: {rps[npc_choice]}")
        print("It's a Draw")
    # Conditions where NPC wins
    elif user_choice == 2 and npc_choice == 0:
        print(f"You Chose {rps_list[user_choice]}: {rps[user_choice]}")
        print(f"NPC Chose {rps_list[npc_choice]}: {rps[npc_choice]}")
        print("NPC wins!")
    elif user_choice == 0 and npc_choice == 1:
        print(f"You Chose {rps_list[user_choice]}: {rps[user_choice]}")
        print(f"NPC Chose {rps_list[npc_choice]}: {rps[npc_choice]}")
        print("NPC wins!")
    elif user_choice == 1 and npc_choice == 2:
        print(f"You Chose {rps_list[user_choice]}: {rps[user_choice]}")
        print(f"NPC Chose {rps_list[npc_choice]}: {rps[npc_choice]}")
        print("NPC wins!")
    # Otherwise, the user wins
    else:
        print(f"You Chose {rps_list[user_choice]}: {rps[user_choice]}")
        print(f"NPC Chose {rps_list[npc_choice]}: {rps[npc_choice]}")
        print("You win!")
# if user input is invalid Not 0, 1 or 2
else:
    print("Invalid choice. Please run the game again and choose 0, 1, or 2.")