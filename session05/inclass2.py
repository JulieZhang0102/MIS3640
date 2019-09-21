import turtle
import math

shape = turtle.Turtle()

shape.pensize(8)

def circle(t, r, angle):
    circumference = 2 * math.pi * r
    m = int(circumference / 2) + 1
    step_length = circumference / m
    step_angle = angle / m
    for i in range(m):
        t.fd(step_length)
        t.lt(step_angle)

def arc1(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    m = int(arc_length / 2) + 1
    step_length = arc_length / m
    step_angle = angle / m
    t.lt(180)
    for i in range(m):
        t.fd(step_length)
        t.rt(step_angle)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    m = int(arc_length / 2) + 1
    step_length = arc_length / m
    step_angle = angle / m
    for i in range(m):
        t.fd(step_length)
        t.lt(step_angle)

def move_left(t, angle, length):
    shape.penup()
    t.lt(angle)
    t.fd(length)
    t.lt(angle)
    shape.pendown()

def move_right(t, angle, length):
    shape.penup()
    t.rt(angle)
    t.fd(length)
    t.lt(angle)
    shape.pendown()

# def circle2(t, r, angle):
#     circumference = 2 * math.pi * r
#     m = int(circumference / 2) + 1
#     step_length = circumference / m
#     step_angle = angle / m
#     for i in range(m):
#         t.fd(step_length)
#         t.lt(step_angle)


circle(shape, 200, 360)
arc1(shape, 100, 180)
arc2(shape, 100, 180)
move_left(shape, 90, 200/3*2)
circle(shape, 100/3, 360)
move_right(shape, 90, 200)
circle(shape, 100/3, 360)

turtle.mainloop()