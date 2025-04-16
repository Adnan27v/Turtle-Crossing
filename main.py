import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)
screen.register_shape("car.gif")

turtle = Player()
scoreboard = Scoreboard()
carManager = CarManager()

screen.listen()

screen.onkey(turtle.up, "w")
screen.onkey(turtle.up, "Up")

game_is_on = True
num = 0


while game_is_on:

    if num%6 == 0:
        carManager.create_car()
    
    carManager.car_move(carManager.allcars)

    num += 1

    time.sleep(0.1)
    screen.update()

    #Reset turtle if crosses finish line and update level
    turtle.reset()
    scoreboard.update_level(turtle.level)
    

    #turtle collision with car
    for car in carManager.allcars:
        if turtle.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            break

screen.exitonclick()
