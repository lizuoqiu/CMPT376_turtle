import turtle
import random

if __name__ == '__main__':

    little_turtle = turtle.Turtle()
    counter = 1
    length = 50
    little_turtle.speed(0)
    while counter < 50:
        r = random.randint(0, 255) / 255
        g = random.randint(0, 255) / 255
        b = random.randint(0, 255) / 255
        little_turtle.color(r, g, b)

        little_turtle.forward(length)
        little_turtle.right(89)
        length = length + 1

    turtle.done()
