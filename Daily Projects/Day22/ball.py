from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.pu()
        self.x = 0
        self.y = 0
        self.speed_x = 8
        self.speed_y = 8
        
        
    def move_ball(self):
        self.x += self.speed_x
        self.y += self.speed_y
        self.goto(self.x, self.y)
        
        
    def bounce_ball_x_axis(self):
        self.speed_x *= -1
        
        
    def bounce_ball_y_axis(self):
        self.speed_y *= -1
        
        
    def reset_ball(self):
        self.x = 0
        self.y = 0
        self.speed_x = 8
        self.speed_y = 8
        self.bounce_ball_x_axis()
        
        
    def increase_speed(self):
        self.speed_x += 2.5
        self.speed_y += 2.5
        
