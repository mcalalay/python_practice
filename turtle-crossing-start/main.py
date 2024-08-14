import time
from turtle import Screen
from player import Player, FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(player.move, "space")

game_is_on = True
while game_is_on:
    time.sleep(player.game_speed)
    screen.update()

    car_manager.create_car()
    car_manager.auto_move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.distance(0, FINISH_LINE_Y) == 0:
        scoreboard.add_level()
        player.refresh()

screen.exitonclick()

