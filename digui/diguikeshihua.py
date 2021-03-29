#递归可视化

import turtle  #海龟作图系统
import time
#--------------------------正方形
# t = turtle.Turtle()
# t.pencolor("blue")
# for i in range(4):
#     t.forward(100)
#     t.right(90)
#     time.sleep(1)
# t.hideturtle()      #隐藏海龟

# turtle.done()

#---------------------------------
t = turtle.Turtle()
t.pencolor("red")
def luoxuanxian(t,line):
    if line > 0:
        t.forward(line)
        t.right(90)
        luoxuanxian(t,line - 5)

luoxuanxian(t,150)
turtle.done()
