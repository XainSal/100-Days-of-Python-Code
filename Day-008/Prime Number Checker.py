# My Method 1
def prime_checker(number):
    prime = True
    if number > 1:
        for x in range(2, number):
            if number % x < 1:
                prime = False
                break
    else:
        prime = False

    if prime == True:
        print(f"{number} is a Prime number.")
    else:
        print(f"{number} is Not a Prime Number.")


# My Method 2
def prime_checker2(number):
    if number > 1:
        if number == 2 or number == 3:
            print(f"{number} is a Prime Number.")
        elif number % 2 == 0 or number % 3 == 0:
            print(f"{number} is Not a Prime Number.")
        else:
            print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is Not a Prime Number.")


# Course Method
def prime_checker3(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker3(number=n)

# For Checking
#for x in range(1, 100):
#    prime_checker3(x)