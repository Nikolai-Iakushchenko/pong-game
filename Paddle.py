from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(1,5)
        self.left(90)
        self.penup()
        self.goto(350, 0)

    def up(self):
        self.setheading(90)
        self.fd(20)

    def down(self):
        self.setheading(270)
        self.fd(20)
