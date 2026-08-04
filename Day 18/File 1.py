from turtle import Turtle, Screen
import random

tim = Turtle()

screen = Screen()
tim.shape("turtle")
colors = ['green yellow','sandy brown', 'olive drab' ,'indian red' , 'purple' , 'pale violet red' , 'turquoise' , 'yellow']

"""Dotted line"""
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()


# """Pentagon"""
# for i in range(5):
#     tim.forward(100)
#     tim.left(72)

# """Hexagon"""
# for i in range(6):
#     tim.forward(100)
#     tim.left(60)

# def draw_shapes(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)

# for shape_side_n in range(3,11):
#     tim.color(random.choice(colors))
#     draw_shapes(shape_side_n)

"""Random Walk"""
directions = [0,90,180,270]
speed = ["fastest" , "fast" , "normal"]
for _ in range(250):
    tim.color(random.choice(colors))
    tim.pensize(15)
    tim.speed(random.choice(speed))
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen.exitonclick()

