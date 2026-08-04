import turtle as t
import random
from turtle import Screen

tim = t.Turtle()
t.colormode(255)
screen = t.Screen()


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

directions = [0,90,180,270]
speed = ["fastest" , "fast" , "normal"]

#random color walk
# for _ in range(250):
#     tim.color(random_color())
#     tim.pensize(15)
#     tim.speed(random.choice(speed))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

#spirograph

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + 10)


draw_spirograph(5)
screen.exitonclick()