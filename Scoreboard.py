from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.rscore = 0
        self.lscore = 0
        self.penup()
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.lscore, align="center", font=("Arial", 60))
        self.goto(100, 200)
        self.write(self.rscore, align="center", font=("Arial", 60))

    def refreshr(self):
        self.rscore += 1
        self.update()

    def refreshl(self):
        self.lscore +=1
        self.update()