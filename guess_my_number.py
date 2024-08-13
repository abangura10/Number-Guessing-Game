import random

print("\tGuess My Number")

# Random number between 1 and 100
number = random.randint(1, 100)

# Keeps track of guesses
num_of_guesses = 0

guess = None

#Condition if guess is right or wrong
while guess != number:
    try:
        # Ask user to guess number
        guess = int(input("\n-> Guess a number between 1 and 100: "))
        num_of_guesses += 1
        if guess < number:
            print("\nWrong number. (YOU'RE LOW)")
            print(f"Number of Guesses: {num_of_guesses}")
        elif guess > number:
            print("\nWrong number. (YOU'RE HIGH)")
            print(f"Number of Guesses: {num_of_guesses}")
    except ValueError:
        print('\nInvalid Input.')

# If guess is right
print("\nYou got it!")
print(f"Number of Guesses: {num_of_guesses}")
