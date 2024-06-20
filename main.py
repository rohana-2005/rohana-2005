from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong Game")
screen.tracer(0)

tim = Turtle()
tim.goto(0, 300)
tim.color("white")
tim.setheading(270)
for i in range(15):
    tim.forward(20)
    tim.penup()
    tim.forward(20)
    tim.pendown()

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
l_score = Score((-200, 150))
r_score = Score((200, 150))


game = True
while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()
    if ball.xcor() > 380:
        ball.reset()
        l_score.l_update()
    if ball.xcor() < -380:
        ball.reset()
        r_score.r_update()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_pad()
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_pad()



screen.exitonclick()
