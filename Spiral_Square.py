import turtle

wn=turtle.Screen()

wn.bgcolor("light blue")
wn.title("Turtle")
sk=turtle.Turtle()
sk.color("blue")

def sqrfunc(size):
  for i in range(4):
    sk.fd(size)
    sk.left(90)
    size=size-5
    
sqrfunc(146)
sqrfunc(126)
sqrfunc(106)
sqrfunc(86)
sqrfunc(66)
sqrfunc(46)
sqrfunc(26)
sqrfunc(6)
sqrfunc(24)
sqrfunc(44)
sqrfunc(64)
sqrfunc(84)
sqrfunc(104)
sqrfunc(124)
sqrfunc(144)
