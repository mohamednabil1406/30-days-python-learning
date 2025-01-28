from turtle import *

right(90)
pos = [(-40, 0), (40, 0)]

for x, y,in pos:
    up()
    goto(x, y)
    down()
# its the left n 
fillcolor('red')
begin_fill()
for i in range(2):       
    forward(200)
    left(90)
    forward(40)      
    left(90)
end_fill()


up()
goto(-40, 0)
down()
left(22)
begin_fill()
for i in range(2):
    forward(217)
    left(68)
    forward(40)
    left(112)
end_fill()

fillcolor('red')
begin_fill()
for k in range(2):
    forward(20)
    right(90)
    forward(40)
    right(90)
end_fill()

done()
