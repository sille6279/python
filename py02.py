# Sille 11.11.2026
#Rõngad
import turtle

aken = turtle.Screen()

aken.setup(width=500, height=400)
aken.title("Sille - Olümpiarõngad")

# Ring 1
turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.pencolor("blue")
turtle.colormode(255)
turtle.fillcolor(0,0,255)
turtle.begin_fill()
turtle.color("blue")
turtle.pensize(6)
turtle.circle(50)

# Ring 2
turtle.penup()
turtle.goto(-90,3)
turtle.pendown()
turtle.pencolor("yellow")
turtle.begin_fill()
turtle.pensize(6)
turtle.circle(50)

# Ring 3
turtle.penup()
turtle.goto(90,-3)
turtle.pendown()
turtle.pencolor("black")
turtle.begin_fill()
turtle.pensize(6)
turtle.circle(50)

turtle.done()