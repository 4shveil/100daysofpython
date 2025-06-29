from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()

paddle_1 = Paddle(350)
paddle_2 = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.onkey(paddle_1.go_up, "Up")
screen.onkey(paddle_1.go_down, "Down")
screen.onkey(paddle_2.go_up, "w")
screen.onkey(paddle_2.go_down, "s")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    ball.move_ball()
    
    if paddle_1.distance(ball) < 50 and ball.xcor() > 320 or paddle_2.distance(ball) < 50 and ball.xcor() < -320:
        ball.bounce_ball_x_axis()
        ball.bounce_ball_y_axis()
        ball.increase_speed()
        
    # check wall collision x axis, point...
    if ball.xcor() > 400:
        scoreboard.l_point()
        ball.reset_ball() # score point left side
    
    if ball.xcor() < -400:
        scoreboard.r_point()
        ball.reset_ball() # score point right side
    
    # check wall collision y axis, bounce...
    if ball.ycor() > 284 or ball.ycor() < -284:
        ball.bounce_ball_y_axis()

screen.exitonclick()
