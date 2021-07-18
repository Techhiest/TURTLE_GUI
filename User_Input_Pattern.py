import turtle
import time
import random

print("This program draws shapes based on the number you enter in a uniform pattern.")
num_str=inpput("Enter the side number of shape you want to draw: ")

if num_str.isdigit():
  squares=int(num_str)
  
angle=180-180*(squares-2)/squares

turtle.up

x=0
y=0
tutrle.setpos(x,y)

numshapes=8

for x in range(numshapes):
  turtle.color(random.random(),random.random(),random.random())
  
  x+=5
  y+=5
  
  turtle.forward(x)
  turtle.left(y)
  
  turtle.right(y)
  for i in range(squares):
    turtle.begin_fill()
    turtle.down()
    turtle.forward(40)
    turtle.left(angle)
    turtle.forward(40)
    print(turtle.pos())
    turtle.up()
    turtle.end_fill()
    
    
time.sleep(11)
turtle.bye()
