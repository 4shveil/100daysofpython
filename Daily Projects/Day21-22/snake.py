from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.make_snake()
        self.head = self.snake_segments[0]
        
        
    def make_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    
    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.goto(position)
        new_segment.color("white")
        self.snake_segments.append(new_segment)
    
    
    def extend(self):
        self.add_segment(self.snake_segments[-1].position())
    
    
    def move_snake(self):
        for seg in range(len(self.snake_segments) - 1, 0, -1):
            next_position_x = self.snake_segments[seg - 1].xcor()
            next_position_y = self.snake_segments[seg - 1].ycor()
            self.snake_segments[seg].goto(next_position_x, next_position_y)
        
        self.head.forward(20)
    
    
    def turn_up(self):
        if not self.head.heading() == 270:
            self.head.seth(90)
    
    
    def turn_down(self):
        if not self.head.heading() == 90:
            self.head.seth(270)
    
    
    def turn_left(self):
        if not self.head.heading() == 0:
            self.head.seth(180)
      
        
    def turn_right(self):
        if not self.head.heading() == 180:
            self.head.seth(0)
            
