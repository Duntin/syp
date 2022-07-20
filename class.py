import turtle
import time
import random

delay=0.1
score=0
h_score=0


screen = turtle.Screen()
screen.title("Snake Game")
screen.bgcolor("black")


screen.setup(width=600, height=600)
screen.tracer(0)

seg= []

head=turtle.Turtle()
head.shape("square")
head.color("red")
head.penup()
head.goto(0, 0)
#head.direction = "Stop"

food= turtle.Turtle()
f_color= random.choice(["red","blue","white"])
f_shape= random.choice(["square", "circle", "triangle"])
food.speed(0)
food.shape(f_shape)
food.color(f_color)
food.penup()
food.goto(0, 100)

pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)


def drawscore():
    pen.clear()
    pen.write("Score:{} High Score:{}" .format(score,h_score), align="center", font=("candara", 24, "bold"))

def checksegs():
    for segs in seg:
        if segs.distance(head)<20:
            resetgame()

def move():
    
    for index in range(len(seg)-1, 0, -1):
        x = seg[index-1].xcor()
        y = seg[index-1].ycor()
        seg[index].goto(x,y)
    if len(seg) > 0:
        x= head.xcor()
        y= head.ycor()
        seg[0].goto(x,y)
    if head.direction=="up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)

def turn(direc):
    if direc =="left" and head.direction == "right":
        return
    if direc =="right" and head.direction == "left":
        return
    if direc =="up" and head.direction == "down":
        return
    if direc =="down" and head.direction == "up":
        return
    head.direction = direc

def checkfood(food):
    global score, delay, h_score
    if head.xcor()==food.xcor() and head.ycor()==food.ycor():
        x= random.randint(-10,10)
        y= random.randint(-10,10)
        food.setx(x*20)
        food.sety(y*20)
        newSeg = turtle.Turtle()
        newSeg.speed(0)
        newSeg.shape("square")
        newSeg.penup()
        newSeg.color("orange")
        seg.append(newSeg)

        score+=10
        if score>h_score:
            h_score=score
        delay-= 0.001

def checkwalls():
    x= head.xcor()
    y= head.ycor()
    if x> 300 or x<-300:
        resetgame()
    if y>300 or y<-300:
        resetgame()

def resetgame():
    global score, delay, seg
    time.sleep(1)
    head.goto(0,0)
    head.direction="Stop"
    score =0
    delay=0.1
    for segs in seg:
        segs.goto(1000, 1000)
    seg= []



screen.listen()
screen.onkey(lambda: turn("left"), 'Left')
screen.onkey(lambda: turn("right"), 'Right')
screen.onkey(lambda: turn("up"), 'Up')
screen.onkey(lambda: turn("down"), 'Down')


while True:
    screen.update()
    move()
    time.sleep(delay)
    checkfood(food)
    checkwalls()
    checksegs()
    drawscore()
    
    
    
screen.mainloop()