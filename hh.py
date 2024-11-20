# This app thinks of a random colour and prompts the user to guess what the colour is . It checks to see if the user's matches the colours the colour it thinks about as well as counts the number of guesses.

import random as r

colour_list = ['red','blue',] # a list of colour the app chooses from

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




import turtle
import random

turtles = list()

def setup():
    global turtle
    start_line = -470

    turtle_color = ['red','blue','green','yellow','purple']
    turtle_ycor =[-20,0,20,40,-40]
    race_screen = turtle.Screen()
    race_screen.setup(1290,720)
    race_screen.bgpic('files/racetrack2.gif')

    for i in range(0,len(turtle_ycor)):
        new_turtle = turtle.Turtle()
        new_turtle.shape('turtle')
        new_turtle.color(turtle_color[i])
        new_turtle.penup()
        new_turtle.setpos(start_line,turtle_ycor[i])
        turtles.append(new_turtle)


def race():
    global turtles
    finishline = 590
    winner = False

    while not winner:
        for current_turtle in turtles:
            move = random.randint(5,12)
            current_turtle.forward(move)
            xcor = current_turtle.xcor()

            if (xcor >=finishline):
                winner = True
                winner_color = current_turtle.color()
                print(f"{winner_color[0]} turtle wins!")

setup()
race()
turtle.mainloop() 