from turtle import Turtle
from random import choice

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class BlockEnemies:
    def __init__(self):
        self.enemies = []
        self.enemy_number = 105
        self.enemy_width = 50
        self.initial_x = SCREEN_WIDTH / 2 + self.enemy_width
        self.initial_y = SCREEN_HEIGHT / 2 - 200
        self.tutle_colours = ["#E60C90", "#98BDDC", "#6B5BCF", "#4FC798", "#CA8725", "#EC7F9B", "#1348ED", "#B9C477"]
        self.row_width = 15
        self.generate_blocks()

    def generate_blocks(self):
        def create_block(coordinates: tuple, colour):
            turtle = Turtle()
            turtle.penup()
            turtle.color(colour)
            turtle.shape("square")
            turtle.shapesize(stretch_wid=1, stretch_len=2.3)
            turtle.setheading(0)
            turtle.goto(coordinates)
            return turtle

        x = self.initial_x
        y = self.initial_y
        x_incrument = self.enemy_width
        for _ in range(self.enemy_number):
            new_block = create_block((x, y), choice(self.tutle_colours))
            self.enemies.append(new_block)
            x -= x_incrument
            if len(self.enemies) % 15 == 0:
                y += self.enemy_width * 1/2
                x += x_incrument
                x_incrument *= -1
