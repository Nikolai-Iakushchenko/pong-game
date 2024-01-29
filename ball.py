from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.up()
        self.speed(0)
        self.lt(20)
        self.x_direction = 10
        self.y_direction = 10

    def move(self):
        if self.xcor() == 380 or self.xcor() == - 380:
            self.x_direction = - self.x_direction
        elif self.ycor() == 280 or self.ycor() == -280:
            self.y_direction = - self.y_direction

        nex_x = self.xcor() +  self.x_direction
        nex_y = self.ycor() +  self.y_direction
        self.goto(nex_x, nex_y)
