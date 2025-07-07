from turtle import *

def input_data():
    x, y = map(int, input('이동할 좌표(x, y)').split())
    return x, y 

# 이동함수
def moving():
    a, b = map(int, input('종류(3이상) 한변(5이상)').split())
    return a, b

# 도형 그리기
def polygon(n, b):
    for i in range(n):
        fd(b)
        lt(360 / n)

# 메인
print('===도형 그리기===')
while True:
    x, y = input_data()
    up()
    goto(x, y)
    down()

    n, b = moving() 
    polygon(n, b)

    con = int(input('계속(1) 중단(그 외)'))
    if con != 1:
        break

exitonclick()