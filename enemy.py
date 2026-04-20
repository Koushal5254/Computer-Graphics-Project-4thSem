import turtle
import random

class EnemyCar:
    def __init__(self):
        self.all_enemies = []

    def create_enemy(self):
        if random.randint(1, 6) == 1:
            new_car = turtle.Turtle()

            new_car.shape("car")
            new_car.color("red")   # 🔴 enemy red
            new_car.penup()

            new_car.setheading(270)  # 🔥 move downward

            x_pos = random.choice([-200, -100, 0, 100, 200])
            new_car.goto(x_pos, 300)

            self.all_enemies.append(new_car)

    def move(self):
        for car in self.all_enemies:
            car.forward(20)