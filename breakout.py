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
# mountain_dew_platform.jpg -> 144 x 46 
 
doritos_size = [50, 77]
mountain_dew_size = [50, 82]
platform_size = [144, 46]

tracer(0)
screen = Screen()

canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
SCREEN_WIDTH = canvas.winfo_width()/2 # here we get canvas(screen) width
SCREEN_HEIGHT = canvas.winfo_height()/2 # here we get the canvas(screen) height

brick_width = 4
brick_height = 2

doritos = "Images/doritos.gif"
mountain_dew = "Images/mountain_dew.gif"
platform_image= "Images/mountain_dew_platform.gif"

turtle.addshape(doritos)
turtle.addshape(mountain_dew)
turtle.addshape(platform_image)

ht()

setup(width, height)

class Brick(Turtle):
	def __init__(self, x, y, width, height, shape, hp = 1, is_platform = False):
		Turtle.__init__(self)
		self.is_platform = is_platform
		self.hp = hp
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
			self.Destroy()
		if (self.hp == 1):
			self.shape(doritos)

	def Destroy(self):
		self.ht()
		self.goto(9999,9999)

class Doritos(Brick):
	def __init__(self, x, y, hp):
		Brick.__init__(self, x, y, doritos_size[0] , doritos_size[1], doritos, hp)
		self.width = doritos_size[0]
		self.height = doritos_size[1]

class MountainDew(Brick):
	def __init__(self, x, y ,hp):
		Brick.__init__(self, x, y, mountain_dew_size[0] , mountain_dew_size[1], mountain_dew, hp)
		self.width = mountain_dew_size[0]
		self.height = mountain_dew_size[1]

class Platform(Brick):
	def __init__(self, x, y):
		Brick.__init__(self, x, y, platform_size[1], platform_size[0], platform_image, 9999,True)
		self.width = platform_size[0]
		self.height = platform_size[1]

	def Move(self, acc_x):
		self.goto(self.xcor() + acc_x, self.ycor())
		self.move()



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
		self.last_brick = None
	
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
		for brick in bricks:
			hit = False
			left = brick.left_side()
			right = brick.right_side()
			bottom = brick.bottom_side()
			top = brick.top_side()

			if self.top_side() < top and self.bottom_side() > bottom:
				if self.right_side() > left and self.left_side() < right:
					hit = True
					struck = "x"

				elif self.left_side() < right and self.right_side() > left:
					hit = True
					struck = "x"

			elif self.right_side() < right and self.left_side() > left:
				if self.top_side() > bottom and self.bottom_side() < top:
					hit = True
					struck = "y"

				elif self.bottom_side() < top and self.top_side() > bottom:
					hit = True
					struck = "y"

			if hit and self.last_brick is not brick:
				brick.Hit()
				self.last_brick = brick
				self.Struck(struck)
