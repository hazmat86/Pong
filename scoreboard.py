from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.up()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))
 
    def l_point(self):
        self.goto(-100, 200)
        self.l_score += 1
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))

    def r_point(self):
        self.goto(100, 200)
        self.r_score += 1
        self.write(self.r_score, align="center", font=("Courier", 30, "normal"))
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 30, "normal"))