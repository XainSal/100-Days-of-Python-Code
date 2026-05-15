import random

alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '-']

print("Welcome to the PyPassword Generator!\n")
total_passwords = int(input("How many passwords would you like to generate?\n"))
total_letters = int(input("How many letters would you like in your password?\n"))
total_symbols = int(input("How many symbols would you like?\n"))
total_numbers = int(input("How many numbers would you like?\n"))

temp_password = []
new_password = []
password =""

print("\nYour passwords are:")
for x in range(0, total_passwords):
    # Reset password containers for each loop iteration
    temp_password = []
    n_password = [""]
    password = ""
    # Gather random components using loops and randint
    for rs in range(0, total_symbols): # random Symbol
        temp_password.append(symbols[random.randint(0, len(symbols) - 1)])

    for rn in range(0, total_numbers): # random Symbol
        temp_password.append(numbers[random.randint(0, len(numbers) - 1)])

    for ra in range(0, total_letters):
        temp_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

    # Shuffle everything thoroughly
    for number in range(0, total_letters + total_numbers + total_symbols):
        temp_password_length = random.randint(0, len(temp_password) - 1)
        n_password.append(temp_password.pop(temp_password_length))

    # Convert list characters directly into a single string
    for text in n_password:
        password += text

    print(password)