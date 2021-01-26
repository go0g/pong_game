from turtle import Screen
from ball import Ball
from paddle import Paddle
from line_draw import Line_Draw
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800


def screen_init():
    my_screen = Screen()
    my_screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    my_screen.bgcolor("black")
    return my_screen


def up_left():
    paddle_left.move_up()


def down_left():
    paddle_left.move_down()


def up_right():
    paddle_right.move_up()


def down_right():
    paddle_right.move_down()


def detect_wall():
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.setheading(360 - ball.heading())


screen = screen_init()
screen.tracer(0)

paddle_left = Paddle(-380)
paddle_right = Paddle(380)
line_drawer = Line_Draw(SCREEN_HEIGHT)
ball = Ball()

screen.update()

screen.onkeypress(up_left, 'w')
screen.onkeypress(down_left, 's')
screen.onkeypress(up_right, 'Up')
screen.onkeypress(down_right, 'Down')

game_run = True
while game_run:
    screen.update()
    screen.listen()
    detect_wall()
    ball.detect_paddle_left(paddle_left)
    ball.detect_paddle_right(paddle_right)
    ball.forward(1)



screen.exitonclick()
