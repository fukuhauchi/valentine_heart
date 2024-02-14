import turtle
from math import cos, sin


def xt(t):
    return 16 * sin(t) ** 3


def yt(t):
    return 13 * cos(t) - 5 * cos(2 * t) - 2 * cos(3 * t) - cos(4 * t)


t = turtle.Turtle()
t.speed(500)
turtle.colormode(255)
turtle.Screen().bgcolor(0, 0, 0)

for i in range(2550):
    t.goto((xt(i) * 20, yt(i) * 20))
    t.pencolor((255 - i) % 255, i % 255, 255)
    t.goto(0, 0)

t.hideturtle()
t.write('NATA I LOVE U')
turtle.update()
turtle.mainloop()
