from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed(0)
        self.lt(20)

    def move(self):
        if not(self.xcor() > 380 or self.xcor() < - 380 or self.ycor() > 280 or self.ycor() < -280):
            self.fd(1)
