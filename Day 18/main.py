import colorgram
import turtle as t
import random
from turtle import Screen

# rgb_colors = []
# colors = colorgram.extract(r'C:\Users\Lenovo\OneDrive\Desktop\Python Files v2\Day 18\image.jpg',30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r,g,b)
#     rgb_colors.append(new_color)

# print(rgb_colors)


color_list = [(221, 232, 225), (208, 160, 81), (55, 89, 132), (145, 91, 40), (139, 26, 48), (222, 208, 104), (132, 177, 203), (45, 55, 104), (158, 45, 84), (169, 159, 39), (128, 189, 143), (84, 20, 44), (38, 43, 66), (186, 94, 106), (189, 138, 166), (84, 124, 182), (60, 39, 30), (79, 153, 165), (87, 157, 90), (195, 79, 72), (160, 201, 220), (45, 74, 77), (79, 74, 43), (59, 125, 113), (218, 176, 188), (167, 207, 166), (220, 181, 168)]
tim = t.Turtle()
t.colormode(255)
tim.penup()
tim.hideturtle()

s = Screen()
tim.speed('fastest')
tim.setheading(225)
tim.forward(250)
tim.setheading(0)
number_of_dots = 100


for dot_count in range(1,number_of_dots+1):
    
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if(dot_count % 10 == 0):
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
s.exitonclick()