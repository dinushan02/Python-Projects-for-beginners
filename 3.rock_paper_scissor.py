# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer to make a choice
# Print choices(emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#    Terminate

# key -> value
# 'r' -> '🪨'
# 's' -> '✂️'

# Use \ to tell Python multiline
# continue keyword, It can is only used inside the loop.

import random

emojis = {'r':'🪨','s':'✂️','p':'📃'}
choices = ("r","p","s")  #List= we can modify,but tuple cannot be modified by remove or append methods. Tuple is just like a read only list.

while True:
    user_choice = input("Rock, paper, or scissors? (r/p/s): ").lower()
    if user_choice not in choices:
        print("Invalid choice!")
        continue  #Use continue statement to jump back to beginning of the while loop

    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_choice == computer_choice:
        print("Tie!")  #Tie = போட்டி சமநிலையில் முடிந்தது
    elif (
        (user_choice == 'r' and computer_choice == 's') or
        (user_choice == 's' and computer_choice == 'p') or
        (user_choice == 'p' and computer_choice == 'r')):
        print("You win")
    else:
        print("You lose")

    should_continue = input("Continue? (y/n): ").lower()
    if should_continue == 'n':
        break


#emojis dict → Gives visual icons for each choice.
#choices tuple → Fixed set of valid inputs (r, p, s).
#while True loop → Keeps game running until the user quits.
#continue → Skips to the next loop if the user enters an invalid choice.
#random.choice(choices) → Lets the computer pick randomly.
#Logic checks → Decides win, lose, or tie.
#Quit condition → User types n when asked.








