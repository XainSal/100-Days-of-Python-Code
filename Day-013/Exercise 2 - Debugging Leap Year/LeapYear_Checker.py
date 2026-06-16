# INCORRECT CODE:
## year = input("Which year do you want to check?")
# if year % 4 == 0:

# ERROR: The input is stored as a string, but '%' (modulus) only works with integers.
# This will cause a TypeError because Python cannot perform mathematical operations on a string.

# FIX: Convert the input into an integer using int()

# CORRECT CODE:
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    # divisible by 4 → could be a leap year
    if year % 100 == 0:
        # divisible by 100 → not a leap year unless...
        if year % 400 == 0:
            # divisible by 400 → leap year
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        # divisible by 4 but not 100 → leap year
        print("Leap year.")
else:
    # not divisible by 4 → not a leap year
    print("Not leap year.")