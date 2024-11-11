import turtle
import random

turtles = list()

def setup():
    global turtle
    start_line = -470

    turtle_color = ['red','blue','green','yellow','black']
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




setup()
turtle.mainloop()