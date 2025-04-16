from turtle import Turtle 
import car_manager

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    
    def __init__(self, shape= "turtle"):
        super().__init__(shape= "turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.starting_position = STARTING_POSITION
        self.level = 1
    
    def up(self):
        self.forward(MOVE_DISTANCE)
    
    def reset(self):
        if self.ycor() >= 280:
            self.goto(self.starting_position)
            self.level += 1
            car_manager.MOVE_INCREMENT += 5
