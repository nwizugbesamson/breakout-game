import random
from turtle import Turtle

BRICK_SHADE = {"3": "red", "4": "green", "5": "blue"}


class Brick:

    def __init__(self):
        self.line = []
        self.wall = []
        self.create_wall()

    def create_brick(self, shade: str, length: int, line: list):
        """create individual bricks

        Args:
            shade (str): color of indivudal brick
            length (int): lenght of individual bricks(3, 4, 5)
            line (dict): dictionary to hold line of bricks
        """
        block = Turtle(shape="square")
        line.append(block)
        block.penup()
        block.color(shade)
        block.shapesize(stretch_wid=1, stretch_len=length)

    def create_line(self, y_pos: int):
        """create single line of brick

        Args:
            y_pos (int): y coordinate of brick line
        """
        line = []
        total = 0
        brick_length = [3, 4, 5]
        while total < 45:
            new_len = random.choice(brick_length)
            new_shade = BRICK_SHADE[str(new_len)]
            self.create_brick(shade=new_shade, length=new_len, line=line)
            total += new_len
        x = -430
        for bl in line:
            y = y_pos
            bl.goto(x, y)
            x += ((bl.shapesize()[1] * 20) + 5)
        self.wall.append(line)

    def create_wall(self):
        """create wall of 5 lines
        """
        for _ in range(100, 225, 25):
            self.create_line(y_pos=_)

    def delete_block(self, touched: Turtle):
        """delete turtle from wall

        Args:
            touched (Turtle): turtle object to be deleted
        """
        for ls in self.wall:
            if touched in ls:
                touched.goto(500, 500)
                ls.remove(touched)
