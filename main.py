import turtle
from math import cos, sin, pi

# Fullscreen the canvas
screen = turtle.Screen()
screen.setup(1.0, 1.0)

# Begin!
t = turtle.Turtle()
yaw = 0

def rotate(vert):
    global yaw
    a = 0.75*yaw
    b = yaw
    c = pi*yaw/3
    x = vert[0]
    y = vert[1]
    z = vert[2]
    row1 = [
        cos(a) * cos(b),
        cos(a) * sin(b) * sin(c) - sin(a) * cos(c),
        cos(a) * sin(b) * cos(c) + sin(a) * sin(c)
    ]
    new_x = x * row1[0] + y * row1[1] + z * row1[2]
    row2 = [
        sin(a) * cos(b),
        sin(a) * sin(b) * sin(c) + cos(a) * cos(c),
        sin(a) * sin(b) * cos(c) - cos(a) * sin(c)
    ]
    new_y = x * row2[0] + y * row2[1] + z * row2[2]
    row3 = [-sin(b), cos(b) * sin(c), cos(b) * cos(c)]
    new_z = x * row3[0] + y * row3[1] + z * row3[2]
    return (new_x, new_y, new_z)


verts = [(-1, -1, -1), (1, -1, -1), (1, 1, -1), (-1, 1, -1), (-1, -1, 1),
         (1, -1, 1), (1, 1, 1), (-1, 1, 1)]
edges = [(0, 1), (1, 2), (2, 3), (3, 0), (0, 4), (1, 5), (2, 6), (3, 7),
         (4, 5), (5, 6), (6, 7), (7, 4)]
scale_factor = 100


def draw_edge(edge):
    a = rotate(verts[edge[0]])
    b = rotate(verts[edge[1]])
    t.pu()
    t.goto(a[0] * scale_factor, a[1] * scale_factor)
    t.pd()
    t.goto((b[0] * scale_factor, b[1] * scale_factor))
    t.pu()


yaw = 0
t.speed(0)
t.hideturtle()
screen.tracer(0)
while True:

    for edge in edges:
        draw_edge(edge)
    screen.update()
    t.clear()
    yaw += (2*pi)/10000

