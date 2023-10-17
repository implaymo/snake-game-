from turtle import Turtle
from random import randint

class Food(Turtle):

    def __init__(self):
        """Creates a circle(food) for snake"""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.new_random_position()

    def new_random_position(self):
        self.goto(randint(-280, 260), randint(-280, 260))