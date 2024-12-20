import turtle

screen = turtle.Screen()
screen.screensize(800,800)
screen.bgcolor('lightsteelblue')


t_ground = turtle.Turtle()
t_ground.penup()
t_ground.pencolor('snow1')
t_ground.fillcolor('snow1')
t_ground.speed(0)
t_ground.goto(-1000,-100)
t_ground.pendown()
t_ground.begin_fill()
t_ground.goto(1000,-100)
t_ground.goto(1000,-1000)
t_ground.goto(-1000,-1000)
t_ground.goto(-1000,-100)
t_ground.end_fill()

t_ground.penup()

t = turtle.Turtle()

t.penup()
t.goto(-100,-140)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(60)
t.end_fill()

#candycane on the tree
candy = turtle.Turtle()

candy.pensize(5)
candy.color("red")
candy.penup()
candy.goto(0, -100)
candy.pendown()
candy.setheading(90)
candy.forward(50)
candy.right(90)
candy.forward(10)
candy.right(90)
candy.forward(10)
candy.penup()
candy.goto(0, -100)
candy.pendown()
candy.end_fill()


t.penup()
t.goto(-100,-40)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(45)
t.end_fill()

# third circle
t.penup()
t.goto(-100,40)
t.pendown()
t.fillcolor('whitesmoke')
t.begin_fill()
t.circle(30)
t.end_fill()

t.penup()
t.goto(-112,75)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(-90,75)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()


t.penup()
t.goto(-100,63)
t.pendown()
t.fillcolor('orange')
t.begin_fill()
t.circle(3)
t.end_fill()



t.penup()
t.goto(-100,50)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-112,55)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-120,63)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-80,63)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()

t.penup()
t.goto(-87,55)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(2)
t.end_fill()


t.penup()
t.goto(-135,0)
t.pendown()
t.fillcolor('goldenrod4')
t.begin_fill()
t.goto(-170, -50)
t.goto(-175, -40)
t.goto(-140,0)
t.goto(-135,0)
t.end_fill()





t.pensize(5)
t.penup()
t.goto(-30,-40)
t.pendown()
t.pencolor("goldenrod4")
t.goto(-65, 0)


t.pencolor('black')

t.penup()
t.goto(-100,-20)
t.pendown()
t.fillcolor('black')
t.begin_fill()
t.circle(3)
t.end_fill()










t = turtle.Turtle()
t.penup()
t.goto(85,-100)
t.pendown()
t.fillcolor("saddle brown")
t.begin_fill()
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)
t.end_fill()

t.penup()
t.pendown()
t.fillcolor("sienna")
t.begin_fill()
t.goto(85,100)
t.goto(185,150)
t.goto(285,100)
t.goto(85,100)
t.end_fill()



t.penup()
t.pencolor('white')
t.goto(300,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.pencolor('white')
t.goto(200,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(100,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(0,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()



t.penup()
t.pencolor('white')
t.goto(-100,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(-200,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


t.penup()
t.pencolor('white')
t.goto(-300,290)
t.pendown()
t.fillcolor('white')
t.begin_fill()
t.circle(100)
t.end_fill()


#words
message="Happy Holidays!"
t.goto(0,310)
t.color('red')
t.write(message,move=False,align='center',font=('Arilal',20,'bold'))































#this is the last line of code
turtle.done()














