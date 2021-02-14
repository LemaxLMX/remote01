#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle
# import time

if __name__ == '__main__':

    turtle.pensize(2)
    turtle.bgcolor("black")
    colors = ["red", "yellow", 'purple', 'blue']
    turtle.tracer(False)  # 关闭绘制过程
    for x in range(400):
        turtle.forward(2 * x)
        turtle.color(colors[x % 4])
        turtle.left(91)
    turtle.tracer(True)
    turtle.done()

print("It's done.")

print('这里是中文')
