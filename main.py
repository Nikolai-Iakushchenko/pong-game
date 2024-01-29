from turtle import Turtle, Screen
from Paddle import Paddle

screen = Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")

paddle = Paddle()

screen.listen()
screen.onkey(paddle.up, 'Up')
screen.onkey(paddle.down, 'Down')

game_is_on = True

while game_is_on:
    screen.update()

screen.exitonclick()