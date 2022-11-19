import random
import turtle
def draw_sq(x,y,z):
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.color(z)
    t.begin_fill()
    for i in range(4):
        t.fd(200);t.rt(90) #200픽셀 전진 후 오른쪽으로 90도 회전
    t.end_fill()

t=turtle.Turtle() #turtle대신 t를 쓴다.
t.shape("turtle") #turtle 모듈의 아이콘을 거북이 모양으로 설정
list=["yellow", "red", "purple", "blue"] #리스트에 저장된 색이 순서대로 표현
for i in range(4):
    draw_sq(random.randint(-100,300),random.randint(-100,300),list[i])
