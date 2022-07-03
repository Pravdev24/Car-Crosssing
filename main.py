import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Car Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move_forward, "Up")
screen.onkey(player.move_backward, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move_cars()

    for i in car.all_cars:
        if player.distance(i) < 20:
            game_is_on = False
            score.game_over()

    if player.ycor() > 280:
        score.increase_level()
        player.starting_position()
        car.level_up()

screen.exitonclick()
