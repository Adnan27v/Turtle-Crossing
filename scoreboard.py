from turtle import Turtle 

FONT = ("Comic Sans MS", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-290, 260)
        self.update_level(1)
    
    def update_level(self,level):
        self.clear()
        self.write(arg= f"Level: {level}", font= FONT, align="left")

    def game_over(self):
        self.goto(0,0)
        self.write(arg= "Game Over", font= FONT, align="center")
