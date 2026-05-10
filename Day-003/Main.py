print('''
*******************************************************************************
                 _____________  _____________   _____________
                 |$ __ $ __ $|  |$ __ $ __ $|   |$ __ $ __ $|
                 | |  | |  | |  | |  | |  | |   | |  | |  | |
                 | |__| |__| |  | |__| |__| |   | |__| |__| |
                 |$ __ $ __ $|  |$ __ $ __ $|   |$ __ $ __ $|
                 | |  | |  | |  | |  | |  | |   | |  | |  | |
                 | |__| |__| |  | |__| |__| |   | |__| |__| |
                 |$____$____$|  |$____$____$|   |$____$____$|
         
*******************************************************************************
''')
print("Welcome to The Lost Isle of Oakhaven.")
print("Your mission: Secure the Heart of the Mountain before the tide rises.\n")

# Step 1: The Jungle Path
choice1 = input('You stand at a fork in the jungle. A muddy path leads "Left" toward the cliffs, '
                'and a dark trail leads "Right" into the thicket. (L/R): ').upper()

if choice1 == "L":
    # Step 2: The Foggy Bay
    choice2 = input('\nYou reach a jagged cliff overlooking the bay. The treasure is on a distant peak. '
                    'Do you "Swim" across the shark-infested waters or "Wait" for the lighthouse ferry? (S/W): ').upper()

    if choice2 == "W":
        # Step 3: The Vault of Echoes
        print("\nThe ferryman drops you at the vault entrance.")
        choice3 = input('Three ancient doors stand before you: '
                        'The "Red" door smells of sulfur, the "Blue" door is freezing to the touch, '
                        'and the "Yellow" door glows with sunlight. Which do you enter? (R/B/Y): ').upper()

        if choice3 == "R":
            print("A hidden trap triggers. Volcanic gas fills the room. Game Over.")
        elif choice3 == "B":
            print("The floor is a thin sheet of ice. You plunge into the freezing abyss. Game Over.")
        elif choice3 == "Y":
            print("\nThe room is filled with gold coins and the Heart of the Mountain. You Win!")
        else:
            print("You hesitated too long and the vault sealed forever. Game Over.")
    else:
        print("The current was too strong and pulled you out to sea. Game Over.")
else:
    print("You stepped on a Camouflaged Viper. Game Over.")