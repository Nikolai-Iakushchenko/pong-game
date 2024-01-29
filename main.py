import time
from turtle import Turtle, Screen

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkeypress(right_paddle.up, 'Up')
screen.onkeypress(right_paddle.down, 'Down')
screen.onkeypress(left_paddle.up, 'w')
screen.onkeypress(left_paddle.down, 's')

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when the ball goes ouf of bounds
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset()


screen.exitonclick()