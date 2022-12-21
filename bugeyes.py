import turtle

turtle.bgcolor("black")
tony = turtle.Pen()
tony.pencolor("green")
for i in range(36):
 tony.circle(i)
 if i%2 > 0:
  tony.left(i * 10)
 else:
  tony.right(i * 10)