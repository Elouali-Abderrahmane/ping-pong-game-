from turtle import Screen
from ball import Ball
from paddle import Paddle
from score import Score
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
START_POSITION = 380
default_time = 0.1


screen = Screen()
screen.bgcolor("black")
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Ping Pong Game")

screen.tracer(0)


r_paddle = Paddle(START_POSITION)
l_paddle = Paddle(-START_POSITION)
ball = Ball()
r_score = Score(40, SCREEN_HEIGHT)
l_score = Score(-40, SCREEN_HEIGHT)

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "a")
screen.onkey(l_paddle.move_down, "z")

game_on = True
while game_on:
    time.sleep(ball.default_speed)
    screen.update()
    ball.goto(ball.xcor() + ball.move_x, ball.ycor() + ball.move_y)

    # If ball collision with y_walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bound_y()
    # If ball collision with the paddle
    if (ball.xcor() >= 360 and ball.distance(r_paddle) <= 50) or (ball.xcor() <= -360 and ball.distance(l_paddle) <= 50):
        ball.bound_x()
        ball.increase_speed()
    # If ball pass the right paddle
    if ball.xcor() >= 400:
        ball.reset_speed_position()
        ball.bound_x()
        l_score.increase_score()
    # If ball pass the left paddle
    if ball.xcor() <= -400:
        ball.reset_speed_position()
        ball.bound_x()
        r_score.increase_score()


screen.exitonclick()
