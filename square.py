import turtle

t = turtle.Turtle()
t.color("black")
t.pensize(3)


t.circle(100)
t.penup()
t.goto(150,0)
t.pendown()

for i in range(4):
    t.forward(100)
    t.right(90)

turtle.done()


