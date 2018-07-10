import turtle
import random
import tkinter
from tkinter import messagebox
    
wn = turtle.Screen()  
wn.bgcolor("#EFECCA")
wn.setup(width=250, height=250) 
turtle = turtle.Turtle()

colors = ["#7D8A2E", "#263248", "#FF8C00", "#F0C600"]  


def play_flake():
    snowflake(8, 6, 0, 0)
    wn.exitonclick()

def snowflake(size, pensize, x, y):
        turtle.penup()
        turtle.goto(x, y)
        turtle.forward(10*size)
        turtle.left(45)
        turtle.pendown()
        turtle.color(random.choice(colors))
        for i in range(8):
          branch(size)
          turtle.left(45)

def branch(size):
    for i in range(3):
        for i in range(3):
            turtle.forward(10.0*size/3)
            turtle.backward(10.0*size/3)
            turtle.right(45)
        turtle.left(90)
        turtle.backward(10.0*size/3)
        turtle.left(45)
    turtle.right(90)
    turtle.forward(10.0*size)

  # leave the window open until you click to close

def hello(name):
  if not name:
    print('Welcome! ' + 'Hello World!')
  else:
    print('Welcome! ' + "Hello " + name)

if __name__ == '__main__':
  input_name = input("Please input a name to continue: ")
  hello(input_name)
  play_flake()
  