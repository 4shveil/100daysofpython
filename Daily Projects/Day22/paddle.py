from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x_pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.y = 0
        self.move_speed = 25
        self.goto(x=x_pos, y=self.y)
        
    def go_up(self):
        if self.ycor() > 260:
            return
        self.y += self.move_speed
        self.goto(x=self.xcor(), y=self.y)
                
    def go_down(self):
        if self.ycor() < -260:
            return
        self.y -= self.move_speed
        self.goto(x=self.xcor(), y=self.y)
