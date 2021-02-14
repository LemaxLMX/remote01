#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from turtle import *

if __name__ == '__main__':

    def stars(n):
        for i in range(0, n):
            fd(100)
            rt(144)

    width(2)
    color('red','yellow')
    speed(0)
    screensize(bg='white')
    tracer(True)

    pu()
    bk(50)
    stars(3)
    lt(180+72)
    pd()

    begin_fill()
    circle(52.5)
    end_fill()
    lt(360-180-72)

    fillcolor("blue")
    begin_fill()
    stars(5)
    end_fill()

    write("It's done, Motherfucker!", font=('Microsoft YaHei UI', 10, "normal"))
    ht()
    tracer(False)
    done()
