'''
請使用def畫出10個，不同顏色的屋頂，及位置的房子
顏色用list用代入
'''
import turtle
import random
turtle.speed(0)
l=['tomato','aquamarine','violet','slategray','blue','yellow','palegreen','steelblue','pink','tan']
for i in range(-1,9):
   def house_roof(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(l[i+1])
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.end_fill()

   def house_body(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color('sienna')
    turtle.begin_fill()
    turtle.setheading(0)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.end_fill()
   a=random.randint(-20,15)
   b=random.randint(-10,20)
   c=random.randint(-15,10)
   d=random.randint(-20,20)
   house_roof(a*b,c*d)
   house_body(a*b,c*d)
