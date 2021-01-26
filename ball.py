from turtle import Turtle
import random


def random_angel():
    rand_angle = random.randint(-10, 10)
    direction = random.choice([True, False])
    if random.choice([True, False]):
        return 180 + rand_angle
    else:
        if rand_angle < 0:
            return 360 - rand_angle
    return rand_angle




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.setheading(random_angel())

    def detect_paddle_left(self, paddle: Turtle):
        if self.xcor() - paddle.xcor() < 20:
            if paddle.ycor() - 40 < self.ycor() < paddle.ycor() + 40:
                self.setheading(180 - self.heading()+random.randint(-10, 10))

    def detect_paddle_right(self, paddle: Turtle):
        if paddle.xcor() - self.xcor() < 20:
            if paddle.ycor() - 40 < self.ycor() < paddle.ycor() + 40:
                self.setheading(180 - self.heading()+random.randint(-10, 10))

    def reset(self):
        self.setposition(0,0)
        self.setheading(random_angel())