import turtle
import time
global p1arr, p2arr, ball, delay
p1arr=[]
p2arr=[]

def resetgame():
    global delay, p1arr, p2arr
    delay=0.08

    for x in range(0,4):
        p1arr[x].goto(-450,20*x)
        p2arr[x].goto(450,20*x)
    ball.goto(0,0)
    ball.dx=-1
    ball.dy=-1
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
print(type(ball))
for x in range (0,4):
    p1arr. append(turtle.Turtle())
    p1arr[x].shape("square")
    p1arr[x].color("blue")
    p1arr[x].penup()
for x in range(0,4):
    p2arr.append(turtle.Turtle())
    p2arr[x].shape("square")
    p2arr[x].color("red")
    p2arr[x].penup()

screen = turtle.Screen()
screen.tracer(0)
screen.title("Pong")
screen.bgcolor("black")
screen.setup(width=1000, height=600)

def movedown(turtlearr):
    for turtle in turtlearr:
        y=turtle.ycor()
        if y> -270:
            turtle.sety(turtle.ycor()-20)
        else: return

def moveup(turtlearr):
    for turtle in reversed(turtlearr):
        y=turtle.ycor()
        if y< 270:
            turtle.sety(turtle.ycor()+20)
        else: return

def p1moveup():
    moveup(p1arr)
def p1movedown():
    movedown(p1arr)
def p2moveup():
    moveup(p2arr)
def p2movedown():
    movedown(p2arr)


def moveball(ball):
    global delay, p1arr, p2arr
    x=ball.xcor()
    y=ball.ycor()
    if(y+20*ball.dy > 300 or y + 20*ball.dx < -300):
        ball.dy = -ball.dy

    for p1 in p1arr:
        if ball.distance(p1) < 30:
            print("h")
            ball.dx = -ball.dx
            delay -= 0.0001
    for p2 in p2arr:
        if ball.distance(p2) < 30:
            print("j")
            ball.dx = -ball.dx
            delay -= 0.0001
    ball.setx(x+10*ball.dx)
    ball.sety(y+10*ball.dy)

screen.listen()
screen.onkeypress(p1moveup,'w')
screen.onkeypress(p1movedown,'s')
screen.onkeypress(p2moveup,'Up')
screen.onkeypress(p2movedown,'Down')

resetgame()
while True:
    screen.update()
    moveball(ball)
    if ball.xcor() > 500 or ball.xcor() < -500:
        resetgame()
    time.sleep(delay)

screen.mainloop()