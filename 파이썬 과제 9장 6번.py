import random #터틀모듈
import turtle #랜덤모듈
def draw_star(x,y,z): #함수정의
        t.penup()
        t.goto(x,y) #좌표이동
        t.pendown()
        t.color(z)
        t.begin_fill()
        r=random.randint(1,100)
        t.lt(110)
        for i in range(5): #도형그리기
                t.fd(r);t.rt(144)
        t.end_fill()

t=turtle.Turtle()
s=turtle.Screen(); s.bgcolor("black")
t.shape("turtle")
list=["yellow","red","purple","blue","green","navyblue","white"] #색 리스트
for i in range(20):
    ra=random.randint(0,6)
    draw_star(random.randint(-200,200),random.randint(-200,200),list[ra]) #랜던 좌표및 길이 랜덤으로 지정
