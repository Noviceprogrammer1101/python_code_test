import turtle
import random

turtle.bgpic("校徽背景.png")
p = turtle.Turtle()
# 原点位移
Len = 150
# 画笔粗细
pen_size = 4
p.speed(0)
p.penup()
p.pensize(pen_size)
p.left(90)
p.backward(Len)
o1 = p.pos()
p.pendown()
p.lt(90)
p.fd(20)
o2 = p.pos()
p.fillcolor('red')
p.begin_fill()


# 左下角书页


def rt_shuye(a, x):
    for i in range(x):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.3
            p.rt(3)
            p.fd(a)
        else:
            a = a - 0.

            p.rt(3)
            p.fd(a)


def lt_shuye(a, x):
    for i in range(x):
        if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
            a = a + 0.3
            p.lt(3)  # 向左转3度
            p.fd(a)  # 向前走a的步长
        else:
            a = a - 0.3
            p.lt(3)
            p.fd(a)


p.rt(90)
lt_shuye(1, 35)  # 绘制书页
p.rt(104.5)
p.fd(20)
x1 = p.pos()  # 左下书坐标
a = 9.1
p.rt(75)

for j in range(18):
    a = a + 0.3
    p.rt(3)
    p.fd(a)

o3 = p.pos()
p.seth(-90)
p.fd(40)
p.lt(90)
p.fd(20)
p.lt(88)

# 右下角书页
p.seth(90)
a = 1
rt_shuye(1, 35)  # 绘制书页
p.lt(104.5)
p.fd(20)
x2 = p.pos()  # 右下书坐标
a = 9.1
p.lt(75)
for j in range(18):
    a = a + 0.3
    p.lt(3)
    p.fd(a)
p.end_fill()
p.seth(90)
p.fd(220)
o = p.pos()  # 书顶坐标

# 右上角书页
a = 1
for i in range(35):
    if 0 <= i < 30 or 60 <= i < 90:
        a = a + 0.3
        p.rt(3)
        p.fd(a)
    else:
        a = a - 0.3
        p.rt(3)
        p.fd(a)
x3 = p.pos()  # 右上书坐标
p.goto(x2)

p.penup()
p.goto(o)
p.seth(90)
p.pendown()
# 左上角书页
a = 1
for i in range(35):
    if 0 <= i < 30 or 60 <= i < 90:  # 控制a的变化
        a = a + 0.3
        p.lt(3)  # 向左转3度
        p.fd(a)  # 向前走a的步长
    else:
        a = a - 0.3
        p.lt(3)
        p.fd(a)
x4 = p.pos()
p.goto(x1)
p.penup()
# p.goto(x3)
# p.pendown()
# p.goto(x2)
p.penup()
p.goto(0, -148)
p.begin_fill()
p.goto(-20, -147)
p.goto(0.10, -109.83)
p.end_fill()
""""
p.penup()
p.goto(-150, -40)
p.write("GUET", font=("方正舒体", 20, "normal"))

"""

xx1 = "正德厚学"
xx2 = "笃行致新"
for i in range(4):
    p.penup()
    p.goto(-120 - i * 2.5, 120 - i * 52)
    p.write(xx1[i], font=("方正舒体", 45, "normal"))
for i in range(4):
    p.penup()
    p.goto(60 + i * 2.5, 120 - i * 52)
    p.write(xx2[i], font=("方正舒体", 45, "normal"))
"""
p.penup()
p.goto(-150, -40)
p.write("德", font=("方正舒体", 45, "normal"))
"""


print(x1, x2, x3, x4)
print(o1, o2, o3, )
p.ht()
turtle.done()
