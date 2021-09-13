import turtle

app = turtle.Turtle()

app.shape('turtle')
app.shapesize(1)
# app.speed(20)
app.pencolor('#d459cd')
app.pensize(5)
for i in range(150, 70, -20):
    app.circle(i)
    app.left(90)
    app.penup()
    app.forward(20)
    app.pendown()
    app.right(90)

turtle.done()