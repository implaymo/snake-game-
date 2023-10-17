from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.pencolor("white")
        self.hideturtle()
        self.high_score = 0
        self.score = 0
        self.goto(0, 270)
        self.update_scoreboard()

    def count_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        return self.write(f"Score: {self.score} High score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset_scoreboard(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

