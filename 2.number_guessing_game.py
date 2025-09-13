# Generate a random number
# Loop
    # Ask the user to make a guess
    # If not a valid number
    #    Print an error
    # If number < guess
    #    Print too low
    # If number > guess
    #    Print too high
    # Else
    #    print well done

"""import random  #random module

number_to_guess = random.randint(1,100)  #Always use Descriptive name for variables
while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("Congratulations! You guessed the number")
            break
    except ValueError:
        print("Please enter a valid number")
"""

# To calculate how many attempts the player takes to guess the number,
# you can use a counter variable and increment it every time the user makes a guess.

import random  # random module

number_to_guess = random.randint(1, 100)  # Always use descriptive name for variables
attempts = 0  # Counter for attempts

while True:
    try:
        guess = int(input("Guess the number between 1 and 100: "))
        attempts += 1  # Increment attempt count for each guess

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break
    except ValueError:
        print("Please enter a valid number.")




