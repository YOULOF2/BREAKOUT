from turtle import Screen
from player import Player
from time import sleep
from block import BlockEnemies


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("BREAKOUT")
screen.tracer(0)

player = Player()
player.create_paddle((0, -250))

blocks = BlockEnemies()


screen.listen()
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

game_on = True
while game_on:
    screen.update()

screen.mainloop()
