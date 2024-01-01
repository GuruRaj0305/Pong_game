
from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.inc_x = 10
        self.inc_y = 10
        self.score_l = 0
        self.score_r = 0
        self.ballspeed = 0.1

    def Move(self,x,y):
        new_x = self.xcor() + self.inc_x
        new_y = self.ycor() + self.inc_y
        self.goto(new_x,new_y)


    def Bounce_y(self):
        self.inc_y *= -1


    def Bounce_x(self):
        self.inc_x *= -1

    def refreshspeed(self):
        self.ballspeed = 0.1

    def speedb(self):
        self.ballspeed *= 0.9


    def speedrefresl(self):
        self.ballspeed = 0.1

    def Point_r(self):
        self.goto(0,0)
        self.inc_x *= -1


    def Point_l(self):

        self.goto(0, 0)
        self.inc_x *= -1

