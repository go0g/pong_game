from turtle import Turtle


class Line_Draw(Turtle):
    def __init__(self, screen_hight):
        super().__init__()
        self.screen_hight = screen_hight
        self.draw_line()

    def draw_line(self):
        positive_wall = self.screen_hight / 2
        negative_wall = positive_wall - self.screen_hight
        timmy = Turtle()
        timmy.penup()
        timmy.pencolor('white')
        timmy.shape('square')

        timmy.setheading(270)
        timmy.pensize(5)
        timmy.sety(positive_wall)
        while timmy.ycor() > negative_wall:
            timmy.pendown()
            timmy.forward(20)
            timmy.penup()
            timmy.forward(20)

