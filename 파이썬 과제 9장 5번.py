import random #랜덤모듈
import turtle #터틀모듈
def draw_sq(x,y,z):
        t.penup()
        t.goto(x,y)
        t.color(z)
        t.begin_fill()
        a=random.randint(0,3)
        r=random.randint(1,100)
        if a==0:
            t.circle(r)
        elif a==1:
            for i in range(3):
                t.fd(r);t.rt(120)
        elif a==2:
            for i in range(4):
                t.fd(r);t.rt(90)
        else:
            for i in range(6):
                t.fd(r);t.rt(60)
        t.end_fill()

t=turtle.Turtle() #turtle대신 t를 쓴다.
t.shape("turtle") #turtle 모듈의 아이콘을 거북이 모양으로 설정
list=["yellow","red","purple","blue","green","navyblue"]  #리스트에 저장된 색이 순서대로 표현
for i in range(7):
    draw_sq(random.randint(-200,200),random.randint(-200,200),list[random.randint(0,5)])
