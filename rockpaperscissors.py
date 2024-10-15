# this app plays "rock, paper, scissors game with the user"

# initiate computers choice
import random
choice_list = ['rock','paper','scissors']
app_choice = random.choice(choice_list) #app chooses from the list...
print(app_choice)

# initiate users choice
user_choice = input("welcome to the game. Rock, Paper or Scissors?: ").capitalize()



# entry validation
while user_choice not in ["Rock","Paper","Scissors"]:
    user_choice = input("invalid entry. Enter Rock, Paper or Scissors: ").capitalize()

# compare user entry and user choice and determine winner

if user_choice == app_choice:
    print(f"its a draw! we both chose {app_choice}!")
elif(
    user_choice == "Rock" and app_choice == "scissors" or
    user_choice == "scissors" and app_choice == "Paper" or
    user_choice == "Paper" and app_choice == "Rock"
):
    print(f"you won! you chose {user_choice} and i chose {app_choice}.")
else:
    print(f"i won! you chose {user_choice} and i chose {app_choice}.")