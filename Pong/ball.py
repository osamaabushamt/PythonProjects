from turtle import Turtle
from paddle import Paddle



class Ball(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.speed("slowest")
        self.x_move = 10
        self.y_move = 10

    def move(self):
        newx = self.xcor() + self.x_move
        newy = self.ycor() + self.y_move
        self.goto(newx,newy)

    def bounce(self):
        self.y_move *= -1

    def ball_touched(self):
        self.x_move *= -1

    def keep_moving(self):
        self.forward(0.1)