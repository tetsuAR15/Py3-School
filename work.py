#!/usr/bin/python3
# -*- coding : utf-8 -*-
from turtle inport *
n = 30
a = 1
b = 1
turtle .speed(0)
turtle .penup()
turtle .goto(0, 0)
turtle .pendown()
for i in range(n):
    print(a)
    turtle .forword(a * 2)
    turtle .left(90)
    temp = a + b
    a = b
    b = temp

turtle.hideturtle()#your own code
turtle.done()" Your own code
