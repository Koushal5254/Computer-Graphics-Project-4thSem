import turtle

class PlayerCar(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=2, stretch_len=1)
        self.penup()
        self.goto(0, -250)

    def move_left(self):
        if self.xcor() > -250:
            self.setx(self.xcor() - 40)

    def move_right(self):
        if self.xcor() < 250:
            self.setx(self.xcor() + 40)