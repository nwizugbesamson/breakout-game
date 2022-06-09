from turtle import Screen
from bricks import Brick
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

SLEEP_TIME = 0.15

# screen object
# main user interface
screen = Screen()
screen.title("BREAKOUT")
screen.bgcolor("black")
screen.setup(width=900, height=700, startx=None, starty=0)
screen.tracer(0)

paddle = Paddle()
ball = Ball()
brick_wall = Brick()
score_board = ScoreBoard()

screen.listen()

# Loop for gameplay
game_is_on = True
while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()

    # LOGIC FOR BALL HITTING BRICKS
    for line in brick_wall.wall:
        for block in line:
            if ball.distance(block.pos()) < 30 and block.shapesize()[1] == 3:
                ball.y_reverse()
                brick_wall.delete_block(touched=block)
                score_board.score += 3
                score_board.update_score()
            elif ball.distance(block.pos()) < 40 and block.shapesize()[1] == 4:
                ball.y_reverse()
                brick_wall.delete_block(touched=block)
                score_board.score += 4
                score_board.update_score()
                SLEEP_TIME -= 0.02
            elif ball.distance(block.pos()) < 50 and block.shapesize()[1] == 5:
                ball.y_reverse()
                brick_wall.delete_block(touched=block)
                score_board.score += 5
                score_board.update_score()
                SLEEP_TIME -= 0.008

    # REVERSE BALL WHEN IT HITS X BOUNDARY
    if ball.xcor() >= 430 or ball.xcor() <= -430:
        ball.x_reverse()

    # REVERSE BALL WHEN IT HITS Y BOUNDARY
    if ball.ycor() >= 300:
        ball.y_reverse()

    # REVERSE BALL WHEN IT HITS PADDLE
    if ball.distance(paddle) < 100 and ball.ycor() <= -275:
        ball.y_reverse()

    # REDUCE LIFE WHEN BALL MISSES PADDLE
    if ball.ycor() <= -330:
        ball.start()
        score_board.life -= 1
        score_board.update_score()
        SLEEP_TIME = 0.15
        if score_board.life <= 0:
            score_board.game_over()
            game_is_on = False

    ball.move()

    # paddle controls as event listeners
    screen.onkeypress(key="Right", fun=paddle.move_right)
    screen.onkeypress(key="Left", fun=paddle.move_left)

screen.exitonclick()
