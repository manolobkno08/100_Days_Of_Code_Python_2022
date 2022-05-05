#!/usr/bin/env python3

from turtle import Turtle, Screen

obj = Turtle()
print(obj)

obj.shape("turtle")
obj.color("coral")
obj.forward(100)

my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()
