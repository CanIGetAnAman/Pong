from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.speed("fastest")

    def draw_outline(self):
        self.goto(0, 250)
        self.pensize(width=6)
        self.pendown()
        self.pencolor("white")
        self.forward(400)
        self.setheading(270)
        self.forward(600)
        self.setheading(180)
        self.forward(800)
        self.setheading(90)
        self.forward(600)
        self.setheading(0)
        self.forward(400)

    def update_score(self, x_coordinate):
        self.clear()
        self.goto(x_coordinate, 250)
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def draw_dotted_line(self):
        self.clear()
        self.pensize(width=6)
        self.goto(0, 250)
        self.setheading(270)
        for num in range(0, 15):
            self.pendown()
            self.forward(15)
            self.penup()
            self.forward(26.5)

    def you_win(self, x_cor, winner):
        self.goto(x_cor, 100)
        self.write(f"Player {winner} Wins!", align=ALIGNMENT, font=("Courier", 30, "normal"))
