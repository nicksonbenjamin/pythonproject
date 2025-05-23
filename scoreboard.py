from turtle import Turtle
ALIGNMENT="center"
FONT=('Arial', 8, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("../../OneDrive/Desktop/data.txt") as data:
             self.high_score=int(data.read())
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score Board:{self.score} High Score:{self.high_score}",False, ALIGNMENT, font=FONT)


    def reset(self):
         if self.score > self.high_score:
            self.high_score= self.score
            with open("../../OneDrive/Desktop/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
         self.score=0


        # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER", align="center", font=('Arial', 8, "normal"))
    def increase_score(self):
        self.score +=1
        self.update_scoreboard()


