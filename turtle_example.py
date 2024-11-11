import turtle

turtle1 = turtle.Turtle()
turtle1.shape('turtle')
turtle1.color('red')

turtle2 = turtle.Turtle()
turtle2.shape('turtle')
turtle2.color('blue')

def make_square(the_turtle):
    for i in range(0,4):
        the_turtle.forward(1)
        the_turtle.right(90)
def make_spiral(the_turtle):
    for i in range(0,36):
        make_square(the_turtle)
        the_turtle.right(10)

# make_square(turtle1)
# turtle2.right(45)
# make_square(turtle2)
make_spiral(turtle1)


turtle.mainloop()