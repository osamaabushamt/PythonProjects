from turtle import Screen

import paddle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle(position=(-350, 0))
r_paddle = Paddle(position=(350, 0))
ball = Ball(position=(0, 0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    print(ball.distance(l_paddle))

    #Ball touched the Y axis
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    #Ball made collision with Paddle
    if ball.distance(l_paddle) <30 or ball.distance(r_paddle) < 30:
        ball.ball_touched()
        ball.move()
    else:
        ball.move()

    #detect if the ball went out of bounce
    if ball.xcor() > 340:
        r_score =+1

    elif ball.xcor() < -340:
        l_score =+1

    if r_score == 5:
        print("Right Won")

    elif l_score == 5:
        print("Left Won")

screen.exitonclick()
