from turtle import Turtle


class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(position)
        self.write(f"{self.l_score}", align="center", font=("Courier", 50, "normal"))
        self.write(f"{self.r_score}", align="center", font=("Courier", 50, "normal"))

    def r_update(self):
        self.clear()
        self.r_score += 1
        self.write(f"{self.r_score}", align="center", font=("Courier", 50, "normal"))


    def l_update(self):
        self.clear()
        self.l_score += 1
        self.write(f"{self.l_score}", align="center", font=("Courier", 50, "normal"))
