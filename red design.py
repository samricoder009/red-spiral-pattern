from turtle import *


title("SamriCoder Design")
penup()
goto(-150,100)
pendown()
speed(10)
bgcolor("black")                                                            
color("red")
pensize(4)


for i in range(8):
    left(45)
    for i in range(9):
        forward(120)
        right(90)


hideturtle()
exitonclick()