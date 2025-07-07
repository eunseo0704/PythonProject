from turtle import *

# 키보드로 그림 그리기
d = 10
def turn_right():
    setheading(0) ; fd(d)

def turn_up():
    setheading(90) ; fd(d)

def turn_left():
    setheading(180) ; fd(d) 

def turn_down():
    setheading(270) ; fd(d)

def blank():
    clear()

def keyboard():
    shape("turtle")
    speed(0)
    listen()
    onkeypress(turn_right, "Right")
    onkeypress(turn_up, "Up")
    onkeypress(turn_left, "Left")
    onkeypress(turn_down, "Down")
    onkeypress(blank, "Escape")

# 마우스로 그림 그리기
def mouse():
    speed(0)
    pensize(5)
    ondrag(goto)
    onkeypress(blank, "Escape")
    listen()

# 메인
select = input("키보드(1) 마우스(2): ")
if select == "1":
    keyboard()
elif select == "2":
    mouse()

done()
