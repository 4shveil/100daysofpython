from turtle import Turtle
from scoreboard import Scoreboard
from car_manager import CarManager


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle, CarManager):
    
    
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("dark green")
        self.pu()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        
    
    def move(self):
        self.forward(MOVE_DISTANCE) 
            
            
    def respawn_turtle(self):
        self.goto(STARTING_POSITION)    
