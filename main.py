import turtle
import time
from car import PlayerCar
from enemy import EnemyCar
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Car Racing Game")
screen.tracer(0)

player = PlayerCar()
enemy = EnemyCar()
score = Scoreboard()

# Controls
screen.listen()
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")

game_on = True

while game_on:
    time.sleep(0.05)
    screen.update()

    enemy.create_enemy()
    enemy.move()

    # Collision
    for car in enemy.all_enemies:
        if car.distance(player) < 25:
            score.game_over()
            game_on = False

    score.increase()

screen.mainloop()