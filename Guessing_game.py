# This app thinks of a random colour and prompts the user to guess what the colour is . It checks to see if the user's matches the colours the colour it thinks about as well as counts the number of guesses.

import random as r

colour_list = ['red','green','blue','yellow','orange','white','black'] # a list of colour the app chooses from

# app chooses a random colour
app_choice = r.choice(colour_list)

# define the player guess counter
guesses = 0

# prompt user to guess the colour
while True:
    print("i am thinking of a colour, guess what it is!")
    user_guess = input() # this stores the user's guess

    if user_guess !=app_choice:
        print("you guessed wrong. try again")
        guesses = guesses + 1
        continue
    else:
        break
print(f"guessed right. it took you {guesses} guesses")
