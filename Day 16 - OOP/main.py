# import another_module
#
# print(another_module.another_variable)

from turtle import Turtle, Screen
import tkinter as TK

timmy = Turtle()
timmy.shape("turtle")
timmy.color('red')
timmy.forward(125); timmy.right(450)
print(timmy)

my_screen = Screen()
my_screen.exitonclick()
