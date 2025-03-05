import turtle
import math

# Configurar la pantalla
screen = turtle.Screen()
screen.bgcolor("#262626")

# Configurar la tortuga
t = turtle.Turtle()
t.speed(10)
t.color("#FF0000")
t.pensize(3)

def draw_heart():
    t.penup()
    t.goto(0, -200)
    t.pendown()
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()
    t.penup()
    t.goto(0, 0)
    t.pendown()

def write_text():
    t.penup()
    t.goto(-130, 50)
    t.color("#FFFFFF")
    t.write("Te Amo Jeysel", font=("Arial", 24, "bold"))
    t.hideturtle()

# Dibujar el corazón y escribir el texto
draw_heart()
write_text()

# Mantener la ventana abierta
screen.mainloop()
