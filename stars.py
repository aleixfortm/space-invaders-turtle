from turtle import Turtle
import random


class Star(Turtle):

    def __init__(self, x, y):
        super().__init__()
        self.color('grey')
        self.penup()
        self.shape('circle')
        self.shapesize(random.random() * 0.2)
        self.goto(x, y)