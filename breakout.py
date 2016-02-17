from turtle import *
import turtle
import random
import subprocess
 
cmd = ['xrandr']
cmd2 = ['grep', '*']
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
p2 = subprocess.Popen(cmd2, stdin=p.stdout, stdout=subprocess.PIPE)
p.stdout.close()
 
resolution_string, junk = p2.communicate()
resolution = resolution_string.split()[0]
width, height = resolution.split('x')

width, height = int(width), int(height)

# doritos.gif -> 160 x 231
# mountain_dew.gif -> 162 x 300
 
doritos_size = [160, 231]
mountain_dew_size = [162, 300]

tracer(0)
screen = Screen()

canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
SCREEN_WIDTH = canvas.winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = canvas.winfo_height()/2 # here we get the canvas(screen) height

brick_width = 4
brick_height = 2

doritos = "Images/doritos.gif"
mountain_dew = "Images/mountain_dew.gif"

turtle.addshape(doritos)
turtle.addshape(mountain_dew)

ht()

setup(width, height)

class Doritos():
	def __init__(self, x, y, hp):
		self.brick = Brick(x, y, doritos_size[0] , doritos_size[1], doritos)
		self.width = doritos[0]
		self.height = doritos[1]

class MountainDew():
	def __init__(self, x, y ,hp):
		self.brick = Brick(x, y, mountain_dew_size[0] , mountain_dew_size[1], mountain_dew)
		self.width = mountain_dew_size[0]
		self.height = mountain_dew_size[1]

class Brick(Turtle):
	def __init__(self, x, y, width, height, shape):
		Turtle.__init__(self)
		self.shape(shape)
		self.resizemode('noresize')
		self.showturtle()
		self.penup()
		self.goto(x,y)
		self.width = width
		self.height = height
		# self.hideturtle()


	def move(self):
		self.goto(self.xcor(),self.ycor())

	def left_side(self):
		return self.xcor()-(self.width/2)

	def right_side(self):
		return self.xcor()+(self.width/2)

	def top_side(self):
		return self.ycor()+(self.height/2)

	def bottom_side(self):
		return self.ycor()-(self.height/2)

class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.goto(x,y)
		self.radius = radius * 10
		self.color(color)
		self.dx = dx / 1.3
		self.dy = dy / 1.3
		self.penup()
		self.shape("circle")
		self.shapesize(radius,radius,2)
	
	def goto(self,x,y):
		super(Ball,self).goto(x,y)
		self.x=x
		self.y=y

	def move(self):
		self.x+=self.dx
		self.y+= self.dy
		self.goto(self.x,self.y)
		self.goto(self.x,self.y-self.radius)
		self.pd()
		self.circle(self.radius)
		self.penup()
		self.goto(self.x,self.y+self.radius)

	def left_side(self):
		return self.xcor()-(self.radius)

	def right_side(self):
		return self.xcor()+(self.radius)

	def top_side(self):
		return self.ycor()+(self.radius)

	def bottom_side(self):
		return self.ycor()-(self.radius)

