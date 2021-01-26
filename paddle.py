from turtle import Turtle

STEPP_Y = 15


class Paddle(Turtle):

    def __init__(self, start_position):
        super().__init__()
        self.shape('square')
        self.shapesize(3.0, 1.0, 1)
        self.penup()
        if start_position > 0:
            self.setx(start_position - 10)
        else:
            self.setx(start_position)
        self.color('white')

    def move_up(self):
        new_y_position = self.ycor() + STEPP_Y
        if self.ycor() < 255:
            self.sety(new_y_position)

    def move_down(self):
        new_y_position = self.ycor() - STEPP_Y
        if self.ycor() > - 255:
            self.sety(new_y_position)
