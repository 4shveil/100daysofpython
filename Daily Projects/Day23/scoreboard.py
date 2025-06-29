from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.pu()
        self.update_leaderboard()
        
        
    def increase_level(self):
        self.level += 1
        self.update_leaderboard()
        
        
    def update_leaderboard(self):
        self.clear()
        self.goto(-220, 250)
        self.write(arg=f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        
    
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over...", align=ALIGNMENT, font=FONT)
