import turtle

if __name__ == '__main__':

    little_turtle = turtle.Turtle()

    for i in range(0, 6):
        little_turtle.forward(100)
        little_turtle.right(60)

    turtle.done()