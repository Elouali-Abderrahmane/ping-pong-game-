from turtle import Turtle


class Score(Turtle):
    def __init__(self, x_position, screen_height):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(x_position, (screen_height // 2) - 50)
        self.__score = 0
        self.update_score()

    def update_score(self):
        self.write(f"{self.__score}", font=(
            "courier", 28, "normal"), align="center")

    def increase_score(self):
        self.__score += 1
        self.clear()
        self.update_score()
