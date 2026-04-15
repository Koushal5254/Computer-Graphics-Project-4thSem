import turtle
from car import PlayerCar
from enemy import EnemyCar
from scoreboard import Scoreboard
import time
import random

# Screen setup
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Car Racing Game")
screen.bgcolor("black")
screen.tracer(0)

player = PlayerCar()
enemy = EnemyCar()
score = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_is_on = True

while game_is_on:
    time.sleep(0.05)
    screen.update()

    enemy.create_enemy()
    enemy.move()

    # Collision
    for car in enemy.all_enemies:
        if car.distance(player) < 20:
            score.game_over()
            game_is_on = False

    score.increase()

screen.mainloop()