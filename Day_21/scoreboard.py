from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("./data.txt", mode="r") as data_file:
            self.high_score = int(data_file.read())
        self.color((30, 30, 30))
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("./data.txt", mode="w") as data_file:
                data_file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 10
        self.update_scoreboard()

    def check_score(self):
        if self.score % 100 == 0:
            return True
        else:
            return False
