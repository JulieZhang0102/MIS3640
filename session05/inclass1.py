import turtle
import math

shape = turtle.Turtle()

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
    t.lt(120)
    for i in range(m):
        t.fd(step_length)
        t.rt(step_angle)

def arc2(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    m = int(arc_length / 2) + 1
    step_length = arc_length / m
    step_angle = angle / m
    t.rt(120)
    for i in range(m):
        t.fd(step_length)
        t.rt(step_angle)

def arc3(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    m = int(arc_length / 2) + 1
    step_length = arc_length / m
    step_angle = angle / m
    t.rt(60)
    shape.penup()
    for i in range(m):
        t.fd(step_length)
        t.rt(step_angle)
    shape.pendown()

def arc4(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    m = int(arc_length / 2) + 1
    step_length = arc_length / m
    step_angle = angle / m
    t.rt(60)
    for i in range(m):
        t.fd(step_length)
        t.rt(step_angle)


circle(shape, 200, 360)
arc1(shape, 200, 120)
arc2(shape, 200, 120)
arc2(shape, 200, 120)
arc3(shape, 200, 60)
arc4(shape, 200, 120)
arc2(shape, 200, 120)
arc2(shape, 200, 120)

turtle.mainloop()