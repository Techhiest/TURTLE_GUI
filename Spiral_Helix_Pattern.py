import turtle
loadWindow=turtle.Screen()
turtle.speed(5)

for i in range(10):
  turtle.circle(5*i)
  turtle.circle(-5*i)
  turtle.left(i)
  
turtle.exitonclick()

