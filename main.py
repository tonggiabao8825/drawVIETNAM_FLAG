import time
import matplotlib.pyplot as plt
import numpy as np
import turtle as t
#barodev 
#EPU IT

# frame 

def main():
    bao = t.Turtle()
    bao.fillcolor('red')
    bao.begin_fill()
    for _ in range(2):
        bao.forward(200)
        bao.right(-90)
        bao.forward(300)
        bao.right(-90)
        bao.forward(200)
    bao.end_fill()
    bao.hideturtle()
    time.sleep(2)
    # star u
    bao.penup()  
    bao.goto(25,180)  
    bao.pendown()  

    bao.fillcolor('yellow')
    bao.begin_fill()
    for _ in range(5):
        bao.forward(80)
        bao.right(144)
        bao.forward(80)
        bao.left(72)
    bao.end_fill()
    bao.hideturtle()

    # text 
    bao.penup()
    bao.goto(0,-120)
    bao.color('red')
    bao.write("Chúc mừng ngày Quốc Khánh nước Cộng Hòa Xã Hội chủ nghĩa Việt Nam ",align='center',font='Arial')
    t.done()

if __name__ =='__main__':
    main()
