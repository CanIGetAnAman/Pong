from turtle import Screen
from paddle import Paddle
from scoreboard import ScoreBoard
from ball import Ball
import time
LEFT_PADDLE = (-350, -50)
RIGHT_PADDLE = (350, -50)

screen = Screen()
screen.setup(width=800, height=700)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

ball = Ball()
left_paddle = Paddle(LEFT_PADDLE)
right_paddle = Paddle(RIGHT_PADDLE)
left_score = ScoreBoard()
right_score = ScoreBoard()
dotted_line = ScoreBoard()
outline = ScoreBoard()
winner_text = ScoreBoard()
dotted_line.draw_dotted_line()
outline.draw_outline()


screen.listen()
screen.onkey(right_paddle.up, "o")
screen.onkey(right_paddle.down, "l")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.ball_speed)
    ball.move(ball.ball_speed)
    left_score.update_score(-200)
    right_score.update_score(200)

    # Detect if ball collides with wall and bounce
    if ball.ycor() > 230 or ball.ycor() < -335:
        ball.wall_bounce()

    # Detect if ball collides with either paddle and bounce
    if ball.distance(right_paddle) < 60 and ball.xcor() > 320:
        ball.ball_speed *= 0.9
        ball.right_paddle_bounce(ball, right_paddle)
    elif ball.distance(left_paddle) < 60 and ball.xcor() < -320:
        ball.ball_speed *= 0.9
        ball.left_paddle_bounce(ball, left_paddle)

    # Update score and start ball back in the middle
    if ball.xcor() > 400:
        new_heading = 135
        left_score.score += 1
        left_score.update_score(-200)
        ball.reset_ball(new_heading)
    elif ball.xcor() < -400:
        new_heading = 45
        right_score.score += 1
        right_score.update_score(200)
        ball.reset_ball(new_heading)

    # Detect winner at 7 points and end game
    if left_score.score == 7:
        winner = 1
        winner_text.you_win(-200, winner)
        game_is_on = False
    elif right_score.score == 7:
        winner = 2
        winner_text.you_win(200, winner)
        game_is_on = False






screen.exitonclick()
