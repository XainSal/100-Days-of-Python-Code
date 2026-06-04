from art import logo
import os

def add(n1, n2):
    return  n1 + n2

def subtract(n1, n2):
    return  n1 - n2

def multiply(n1, n2):
    return  n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
    keep_going = True

    while keep_going == True:
        operational_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        calculation_function = operations[operational_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operational_symbol} {num2} = {answer}")

        should_continue = input(f"type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'e' to exit.: ").lower()
        if should_continue == 'y':
            num1 = answer
        elif should_continue == 'n':
            keep_going = False
            os.system('cls||clear')
            calculator()
        elif should_continue == 'e':
            keep_going = False

calculator()