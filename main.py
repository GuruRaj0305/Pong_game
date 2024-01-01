from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from Scoreboard import Score



screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Pong_game")

score = Score()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()




screen.listen()
screen.onkey(l_paddle.goup, "w")
screen.onkey(l_paddle.godown, "s")

screen.onkey(r_paddle.goup, "Up")
screen.onkey(r_paddle.godown, "Down")




game_on = True

while game_on:
    time.sleep(ball.ballspeed)
    screen.update()
    ball.Move(250, 250)
    if 280<ball.ycor() or ball.ycor()<-280:
        ball.Bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.Bounce_x()
        ball.speedb()

    if ball.xcor()<-400:
        ball.Point_r()
        score.refreshr()
        ball.refreshspeed()


    if ball.xcor()>400:
        ball.Point_l()
        score.refreshl()
        ball.refreshspeed()











screen.exitonclick()