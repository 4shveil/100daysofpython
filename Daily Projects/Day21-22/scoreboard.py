from turtle import Turtle
ALIGNMENT = "Center"
FONT = ("FiraMono Nerd Font", 16, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        self.score = 0
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 276)
        self.update_leaderboard()
        
        
    def update_leaderboard(self):
        self.clear()
        self.write(arg= f"Score = {self.score}", move= False, align=ALIGNMENT, font=FONT)
        
        
    def game_over(self):
        self.goto(0,0)
        self.write(arg = "Game over.", align=ALIGNMENT, font=FONT)
        
        
    def add_score(self):
        self.score += 1
        self.update_leaderboard()
        
