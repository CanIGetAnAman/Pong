from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.shapesize(stretch_wid=0.75, stretch_len=0.75)
        self.color("white")
        self.setheading(45)
        self.ball_speed = 0.1

    def move(self, ball_speed):
        # new_x = self.xcor() + 10
        # new_y = self.ycor() + 10
        # self.goto(new_x, new_y)
        self.forward(20)

    def wall_bounce(self):
        current_heading = self.heading()
        if 0 < current_heading < 90:
            new_heading = 360 - current_heading
            self.setheading(new_heading)
        elif 90 < current_heading < 180:
            new_heading = 270 - (current_heading - 90)
            self.setheading(new_heading)
        elif 180 < current_heading < 270:
            new_heading = 180 - (current_heading - 180)
            self.setheading(new_heading)
        else:
            new_heading = 90 - (current_heading - 270)
            self.setheading(new_heading)

    def right_paddle_bounce(self, ball, right_paddle):
        if ball.ycor() - right_paddle.ycor() > 25:
            self.setheading(120)
        elif 0 < (ball.ycor() - right_paddle.ycor()) < 25:
            self.setheading(135)
        elif ball.ycor() - right_paddle.ycor() == 0:
            self.setheading(180)
        elif 0 < abs(right_paddle.ycor() - ball.ycor()) < 25:
            self.setheading(225)
        elif abs(right_paddle.ycor() - ball.ycor()) > 25:
            self.setheading(240)

    def left_paddle_bounce(self, ball, left_paddle):
        if ball.ycor() - left_paddle.ycor() > 25:
            self.setheading(60)
        elif 0 < (ball.ycor() - left_paddle.ycor()) < 25:
            self.setheading(45)
        elif ball.ycor() - left_paddle.ycor() == 0:
            self.setheading(0)
        elif 0 < abs(left_paddle.ycor() - ball.ycor()) < 25:
            self.setheading(315)
        elif abs(left_paddle.ycor() - ball.ycor()) > 25:
            self.setheading(300)

    def reset_ball(self, new_heading):
        self.setheading(new_heading)
        self.ball_speed = 0.1
        self.goto(0, 0)
        time.sleep(3)
