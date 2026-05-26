from art import logo
import os

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] * 4

def caesar(start_text, shift_amount, cipher_mode):
    output_text = ""
    shift_amount = shift_amount % 26
    if cipher_mode == "decode":
        shift_amount *= -1
    for letter in start_text:
        if not letter.isalpha():
            output_text += letter
        else:
            # We start searching from index 26 to safely allow negative shift indexing
            position = alphabets.index(letter, 26)
            output_text += alphabets[position + shift_amount]

    print(f"The {cipher_mode}d text is: {output_text}")

keep_going = "yes"

while keep_going == "yes":
    os.system('cls||clear')
    print(logo)

    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    input_text = input("Type your message:\n").lower()
    shift_number = int(input("Type the shift number:\n"))

    caesar(start_text=input_text, shift_amount=shift_number, cipher_mode=choice)
    
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()

    if keep_going != "yes" and keep_going != "no":
        print("Invalid Choice")
    elif keep_going == "no":
        print("Goodbye")
