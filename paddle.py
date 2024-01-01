
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def goup(self):
        self.newy = self.ycor() + 50
        self.goto(self.xcor(), self.newy)

    def godown(self):
        self.newy = self.ycor() - 50
        self.goto(self.xcor(), self.newy)


