from turtle import *
import random

tracer(0)
canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
SCREEN_WIDTH = canvas.winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = canvas.winfo_height()/2 # here we get the canvas(screen) height

brick_width = 4
brick_height = 2
bricks = []
colors = ['red','green','blue', 'black', 'purple']

class Brick(Turtle):
	def __init__(self, x, y, width, height, color):
		Turtle.__init__(self)
		self.shape("square")
		self.resizemode('noresize')
		self.shapesize(height,width)
		self.showturtle()
		self.color(color)
		self.penup()
		self.goto(x,y)
		self.width = width*20
		self.height = height*20
		self.goto(x-self.width/2,y+self.height/2)
		self.pd()
		self.goto(self.xcor()+self.width,self.ycor())
		self.goto(self.xcor(),self.ycor()-self.height)
		self.goto(self.xcor()-self.width,self.ycor())
		self.goto(x-self.width/2,y+self.height/2)
		self.penup()
		self.goto(x,y)
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
		self.dx = dx
		self.dy = dy
		self.penup()
		#self.getscreen().addshape('paddle.gif')
		#self.shape("paddle.gif")
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

