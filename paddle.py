from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinate):
        super().__init__()
        self.penup()
        self.goto(coordinate)
        self.setheading(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)

    # def create_paddle(self, x_coordinate):

    def up(self):
        if self.ycor() < 190:
            self.setheading(90)
            self.forward(40)

    def down(self):
        if self.ycor() > -290:
            self.setheading(270)
            self.forward(40)
