import turtle

def register_car():
    # 🔥 Top view car shape (simple & clean)
    car_shape = (
        (0, 20),    # front
        (10, 10),
        (10, -20),
        (-10, -20),
        (-10, 10),
        (0, 20)
    )

    turtle.register_shape("car", car_shape)


class PlayerCar(turtle.Turtle):
    def __init__(self):
        super().__init__()

        register_car()

        self.shape("car")
        self.color("blue")   # 🔵 player blue
        self.penup()

        self.setheading(90)  # 🔥 straight upward
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() > -250:
            self.setx(self.xcor() - 40)

    def move_right(self):
        if self.xcor() < 250:
            self.setx(self.xcor() + 40)