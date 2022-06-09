from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xmove = 10
        self.ymove = 10
        self.start()

    def start(self):
        """starting position of ball
        """
        self.goto(0, -250)
        self.move()

    def move(self):
        """method to control turtle movement using goto method
        """
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x, new_y)

    def x_reverse(self):
        """reverse turtle in x direction
        """
        self.xmove *= -1

    def y_reverse(self):
        """reverse trtle in y direction
        """
        self.ymove *= -1
