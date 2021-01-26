from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.player_left = Player(-50, 240)
        self.player_right = Player(50, 240)

    def add_score(self, side):
        if side == "right":
            self.player_right.update_score()
        else:
            self.player_left.update_score()

class Player(Turtle):
    def __init__(self, position_x, position_y):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.setposition(position_x, position_y)
        self.color('white')
        self.write(self.score, move=False,  align="center", font=("Arial", 30, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(self.score, move=False, align="center", font=("Arial", 30, "normal"))
