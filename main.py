import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
pallet = [(253, 252, 241), (238, 250, 244), (187, 18, 44), (243, 231, 66), (252, 235, 239), (210, 236, 242),
          (196, 75, 32), (218, 66, 107), (17, 124, 173), (196, 175, 17), (108, 181, 209), (12, 142, 88), (12, 166, 214),
          (210, 152, 96), (187, 41, 61), (241, 231, 2), (23, 39, 76), (77, 174, 94), (36, 44, 112), (215, 69, 50),
          (218, 130, 155), (124, 185, 119), (235, 165, 183), (5, 58, 39), (146, 209, 220), (8, 95, 55), (4, 86, 111),
          (162, 29, 27), (234, 171, 164), (162, 212, 176)]
toy = Turtle()
toy.speed(10)
toy.setheading(225)
toy.penup()
toy.forward(300)
toy.setheading(0)


def dot_row(size):
    for i in range(size):
        colored = random.choice(pallet)
        toy.dot(20, colored)
        toy.penup()
        toy.forward(50)


for j in range(10):
    dot_row(10)
    toy.left(90)
    toy.forward(50)
    toy.setheading(180)
    toy.forward(500)
    toy.setheading(0)

screen = Screen()
screen.exitonclick()
