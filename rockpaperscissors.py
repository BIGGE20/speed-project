# this app plays "rock, paper, scissors game with the user"

# initiate computers choice
import random
# choice_list = ['rock','paper','scissors']
# app_choice = random.choice(choice_list) #app chooses from the list...

# initiate users choice
# user_choice = input("welcome to the game. Rock, Paper or Scissors?: ").capitalize()


# # entry validation
# while user_choice not in ["Rock","Paper","Scissors"]:
#     user_choice = input("invalid entry. Enter Rock, Paper or Scissors: ").capitalize()

# # compare user entry and user choice and determine winner

# if user_choice == app_choice:
#     print(f"its a draw! we both chose {app_choice}!")
# elif(
#     user_choice == "Rock" and app_choice == "scissors" or
#     user_choice == "scissors" and app_choice == "Paper" or
#     user_choice == "Paper" and app_choice == "Rock"
# ):
#     print(f"you won! you chose {user_choice} and i chose {app_choice}.")
# else:
#     print(f"i won! you chose {user_choice} and i chose {app_choice}.")

# compare user entry and user choice and determine winner

while True:
    rounds = int(input("How many time would you like to play? Enter a number: "))
    if (rounds <2
        or rounds > 10):
        print("enter a number between 2-10. Try again")
        continue
    else:
        print("welcome to the game. Lets play!")

    for round in range(rounds):
        choice_list = ['rock','paper','scissors']
        app_choice = random.choice(choice_list) #app chooses from the list...
        user_choice = input("Rock, Paper or Scissors: ").capitalize()

        # Match the entries and determine a winner
        if user_choice == app_choice:
            print(f"it is a draw! We both chose {app_choice}")
        elif(
            user_choice == "Rock" and app_choice == "Scissors" or
            user_choice == "Paper" and app_choice == "Rock" or
            user_choice == "Scissors" and app_choice == "Paper"
        ):
            print(f"you won. you chose {user_choice} and i chose {app_choice}.")
        else:
            print(f"i won, i chose {app_choice} and you chose {user_choice}.")
    play_again = input(f"you have played {rounds} games. would you like to play again? (yes or no): ")
    if play_again == 'yes'.lower():
        continue
    else:
        print("Thanks for playing. Bye.")
        break