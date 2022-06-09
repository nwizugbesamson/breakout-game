from turtle import Turtle


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=0.7, stretch_len=5)
        self.penup()
        self.goto(0, -300)

    def move_right(self):
        """Paddle right move functionality within screen limit
        """
        if self.xcor() < 380:
            self.fd(30)

    def move_left(self):
        """Paddle left move functionality within screen limit
        """
        if self.xcor() > -380:
            self.bk(30)
