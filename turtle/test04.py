import turtle

app = turtle.Turtle()

app.shape('turtle')
app.shapesize(1)
# app.speed(20)
app.pencolor('#d459cd')
app.pensize(5)
for i in range(0, 4):
    app.forward(50)
    app.left(90)
    app.forward(50)
    app.left(90)
    app.forward(50)
    app.left(90)
    app.forward(50)
    app.left(90)
    app.penup()
    app.forward(100)
    app.pendown()
turtle.done()