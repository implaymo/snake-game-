from turtle import Turtle
import time

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creation of snake body"""
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Creates a segment of a snake"""
        new_snake = Turtle("square")
        new_snake.penup()
        new_snake.color("white")
        new_snake.goto(position)
        self.segments.append(new_snake)

    def extend(self):
        """Extends the body of the snake. Used when snakes eats food"""
        self.add_segment(self.segments[-1].position())

    def snake_move(self):
        """Makes squares follow each other"""
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Moves snake up(90degrees)"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Moves snake down(270degrees)"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        """Moves snake right(0degrees)"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        """Moves snake left(180degrees)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reset_snake(self):
        for seg in self.segments:
            seg.hideturtle()
        time.sleep(0.03)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
