from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 30, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.life = 10
        self.penup()
        self.color("white")
        self.ht()
        self.update_score()

    def game_over(self):
        """update score board on gameover
        """
        self.home()
        self.write(self.write(f"GAME OVER", align=ALIGNMENT, font=FONT))

    def update_score(self):
        self.clear()
        self.goto(x=330, y=290)
        self.write(f"SCORE: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(x=-350, y=290)
        self.write(f"LIVES: {self.life}", align=ALIGNMENT, font=FONT)
