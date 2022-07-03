from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(x=-290, y=270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}", font=("Courier", 15, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 15, "bold"))





