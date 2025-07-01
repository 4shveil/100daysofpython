import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FINISH_LINE_Y = 280


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
cars = CarManager()
scoreboard = Scoreboard()
    
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move_cars()
    cars.make_cars()
    cars.remove_passed_cars()
    
    
    for car in cars.cars_spawned:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False
            break
            
            
    if player.ycor() > FINISH_LINE_Y:
        player.respawn_turtle()
        cars.increase_speed()
        scoreboard.increase_level()
