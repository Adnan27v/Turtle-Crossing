from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.allcars = []

    def create_car(self):
        car = Turtle()
        car.penup()
        car.shape("car.gif")
        car.shapesize(stretch_len=2)
        car.color(choice(COLORS))
        car.goto(-300, randint(-250, 250))
        car.setheading(0)
        car.forward(STARTING_MOVE_DISTANCE)
        self.allcars.append(car)
    
    def car_move(self,all_cars):
        for car in all_cars:
            car.forward(MOVE_INCREMENT)