import turtle;

canvas = turtle.Screen()
canvas.setup(400,200)
canvas.bgcolor('red')

sarah = turtle.Turtle()
sarah.color('yellow')
sarah.shape('turtle')
def draw_square():
    sarah.forward(50)          # make sarah draw a square
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    sarah.forward(50)
    sarah.left(90)
    return

for index in range(0,36):
    draw_square()
    sarah.left(10)
    draw_square()


canvas.exitonclick()