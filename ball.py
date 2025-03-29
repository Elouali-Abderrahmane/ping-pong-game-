from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.move_x = 10
        self.move_y = 10
        self.default_speed = 0.1

    def bound_y(self):
        self.move_y *= -1

    def bound_x(self):
        self.move_x *= -1

    def increase_speed(self):
        self.default_speed *= 0.9

    def reset_speed_position(self):
        self.default_speed = 0.1
        self.goto(0, 0)
