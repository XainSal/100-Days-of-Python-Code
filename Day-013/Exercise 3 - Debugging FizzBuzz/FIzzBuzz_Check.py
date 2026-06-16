# Loop through numbers from 1 to 100
for number in range(1, 101):

    # INCORRECT CODE:
    # if number % 3 == 0 or number % 5 == 0:
    #     print("FizzBuzz")
    # if number % 3 == 0:
    #     print("Fizz")
    # if number % 5 == 0:
    #     print("Buzz")
    # else:
    #     print([number])

    # ERROR: Multiple 'if' statements are used instead of 'if-elif-else'.
    # This causes multiple outputs for the same number (e.g., 15 prints FizzBuzz, Fizz, and Buzz).
    # Also, the 'else' is only attached to the last 'if', not all conditions.
    # Additionally, print([number]) prints a list instead of the number.

    # FIX:
    # 1. Use 'if-elif-else' so only one condition runs per number.
    # 2. Check FizzBuzz (both conditions) first.
    # 3. Replace print([number]) with print(number).

    # CORRECT CODE:
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)