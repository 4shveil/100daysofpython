from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Ssssssssssnake game")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.turn_up, key="Up")
screen.onkey(fun=snake.turn_right, key="Right")
screen.onkey(fun=snake.turn_left, key="Left")
screen.onkey(fun=snake.turn_down, key="Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move_snake()
    
    
    # detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.add_score()
        snake.extend()
        food.refresh()
        
    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
        break
    print(snake.snake_segments[1:-1])
    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        # if head collides with any segments of the tail, trigger game over
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
            break
         
screen.exitonclick()
