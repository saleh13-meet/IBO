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

# doritos.gif -> 50 x 77
# mountain_dew.gif -> 50 x 82
 
doritos_size = [50, 77]
mountain_dew_size = [50, 82]

tracer(0)
screen = Screen()

canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
SCREEN_WIDTH = canvas.winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = canvas.winfo_height()/2 # here we get the canvas(screen) height

brick_width = 4
brick_height = 2

platform_size = [96, 24]

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
		self.brick = Brick(x, y, mountain_dew_size[0] , mountain_dew_size[1], mountain_dew, hp)
		self.width = mountain_dew_size[0]
		self.height = mountain_dew_size[1]

class Platform():
	def __init__(self, x, y):
		self.brick = Brick(x, y + platform_size[1], platform_size[1] / 12, platform_size[0] / 12, "square", True)
		self.width = platform_size[0]
		self.height = platform_size[1]

	def Move(self, acc_x):
		self.brick.goto(self.brick.xcor() + acc_x, self.brick.ycor())
		self.brick.move()

class Brick(Turtle):
	def __init__(self, x, y, width, height, shape, hp = 1, is_platform = False):
		Turtle.__init__(self)
		self.is_platform = is_platform
		self.hp = hp
		self.shapesize(width, height)
		self.shape(shape)
		self.showturtle()
		self.penup()
		self.goto(x,y)
		self.width = width
		self.height = height


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

	def Hit(self):
		self.hp -= 1
		if self.hp <= 0 and not self.is_platform:
			Destroy()

	def Destroy(self):
		self.ht()
		self.goto(9999,9999)


class Ball(Turtle):
	def __init__(self, x, y, dx, dy, radius, color):
		Turtle.__init__(self)
		self.goto(x,y)
		self.radius = radius
		self.color(color)
		self.dx = dx
		self.dy = dy
		self.penup()
		self.shape("circle")
		self.ht()
	
	def goto(self,x,y):
		super(Ball,self).goto(x,y)
		self.x=x
		self.y=y

	def move(self):
		self.clear()
		self.x+=self.dx
		self.y+= self.dy
		self.goto(self.x,self.y)
		self.pd()
		self.begin_fill()
		self.circle(self.radius)
		self.end_fill()
		self.penup()

	def left_side(self):
		return self.xcor()-(self.radius)

	def right_side(self):
		return self.xcor()+(self.radius)

	def top_side(self):
		return self.ycor()+(self.radius)

	def bottom_side(self):
		return self.ycor()-(self.radius)

	def Struck(self, axis):
		if (axis == "x"):
			self.dx *= -1

		if (axis == "y"):
			self.dy *= -1

	def Borders(self, left, right, top, bottom):
		if self.left_side() <= left or self.right_side() >= right:
			self.Struck("x")
		if self.top_side() >= top or self.bottom_side() <= bottom:
			self.Struck("y")

	def HitBricks(self, bricks):
		center_x = self.xcor()
		center_y = self.ycor()		
		for i in bricks:
			hit = False
			left = brick.left_side()
			right = brick.right_side()
			bottom = brick.bottom_side()
			top = brick.top_side()

			if right >= self.left_side() or left <= self.right_side() and center_y <= self.top_side() and center_y >= self.bottom_side():
				self.Struck("y")
				hit = True
			
			if top >= self.bottom_side() or bottom <= self.top_side() and center_x <= self.right_side() and center_x >= self.left_side():
				self.Struck("x")
				hit = True

			if hit:
				brick.Hit()

