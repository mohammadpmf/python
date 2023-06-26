from turtle import *

def f1():
    global my_speed
    my_speed += 1
def f2():
    global my_speed
    my_speed -= 1
def f3():
    global my_turn
    my_turn += 1
    lt(my_turn)
def f4():
    global my_turn
    my_turn -= 1
    lt(my_turn)
def f5():
    global my_size
    my_size+=1
    pensize(my_size)
def f6():
    global my_size
    my_size-=1
    pensize(my_size)
def my_reset():
    global my_size, my_speed, my_turn
    my_speed=0
    my_turn=0
    reset()
    home()
    my_size=1
    seth(0)
    

def red():
    color('red')
def green():
    color('green')
def blue():
    color('blue')
def orange():
    color('orange')
def yellow():
    color('yellow')
def cyan():
    color('cyan')
def white():
    color('white')

onkey(f1, 'Up')
onkey(f2, 'Down')
onkey(f3, 'Left')
onkey(f4, 'Right')
onkey(f5, 'plus')
onkey(f6, 'minus')
onkey(red, 'r')
onkey(green, 'g')
onkey(blue, 'b')
onkey(yellow, 'y')
onkey(cyan, 'c')
onkey(orange, 'o')
onkey(white, 'w')
onkey(up, 'u')
onkey(down, 'd')
onkey(my_reset, 'R')
listen()
my_size = 1
my_speed=0
my_turn=0
while True:
    fd(my_speed)
    lt(my_turn)