# Ask the user to enter a number and convert it to an integer
number = int(input("Which number do you want to check? "))

# INCORRECT CODE:
# if number % 2 = 0:

# ERROR: Used '=' instead of '==' in the condition.
# '=' is an assignment operator, while '==' is a comparison operator.
# This causes a syntax error because Python cannot assign a value inside an if condition.

# FIX: Replace '=' with '==' to correctly compare values.

# CORRECT CODE:
if number % 2 == 0:
    # if remainder is 0 → even number
    print("This is an even number.")
else:
    # If remainder is not 0 → odd number
    print("This is an odd number.")