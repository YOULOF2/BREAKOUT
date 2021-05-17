from turtle import Turtle


class Player:
    def __init__(self):
        self.turtle = Turtle()
        self.movement_amount = 30

    def create_paddle(self, coordinates):
        self.turtle.penup()
        self.turtle.color("white")
        self.turtle.shape("square")
        self.turtle.shapesize(stretch_wid=1, stretch_len=5)
        # self.turtle.setheading(0)
        self.turtle.goto(coordinates)

    def move_left(self):
        new_x = self.turtle.xcor() - self.movement_amount
        self.turtle.goto((new_x, self.turtle.ycor()))

    def move_right(self):
        new_x = self.turtle.xcor() + self.movement_amount
        self.turtle.goto((new_x, self.turtle.ycor()))
