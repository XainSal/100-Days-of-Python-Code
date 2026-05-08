# Creating a greeting for the user using the "print()" function.
print("Welcome to the Band Name Generator.")
# Asking the user for the name of the city they grew up in using the "input()" function and storing the value in the "city_name" variable.
# "\n" creates a new line so the user can type their answer below the question.
city_name = input("What's name of city you grew up in?:\n")
# Asking the user for their pet's name using the "input()" function and storing the value in the "pet_name" variable.
# "\n" creates a new line so the user can type their answer below the question.
pet_name = input("What's the name of your pet:\n")
# Combining both names in different orders to suggest possible band names and displaying the output using the "print()" function.
# "\n" is used to print each band name on a new line.
print("Possible Band Names Could Be:\n1. " + city_name + " " + pet_name + "\n2. " + pet_name + " " + city_name )