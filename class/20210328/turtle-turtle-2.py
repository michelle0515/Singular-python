import turtle as t

t.color('red')
t.shape('turtle')

t.penup()
for i in range(1,1000,1):
  t.stamp()
  t.forward(i)
  t.right(25)
  print(i)