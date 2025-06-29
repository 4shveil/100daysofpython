from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "pink", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    
    def __init__(self):
        self.cars_spawned = []
        self.move_speed = STARTING_MOVE_DISTANCE
        self.make_cars()
        
        
    def make_cars(self):
        if random.randint(0, 11) > 9:
            random_y = random.randint(-200, 225)
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.pu()
            new_car.goto(330, random_y)
            self.cars_spawned.append(new_car)
        
        
    def remove_passed_cars(self):
        for car in self.cars_spawned:
            if car != None and car.xcor() < -360:
                car.clear()
                self.cars_spawned.remove(car)
    
    
    def move_cars(self):
        for car in self.cars_spawned:
            self.current_cor = car.xcor()
            self.current_cor -= self.move_speed
            car.goto(self.current_cor, car.ycor())
            
            
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
