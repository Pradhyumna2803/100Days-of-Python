from turtle import Turtle, Screen
tim = Turtle()
#print(tim)
tim.shape("turtle")
tim.color("green")
for i in range(30):
    tim.forward(100)
    tim.right(500)
    tim.left(200)

my_screen = Screen()
my_screen.exitonclick()