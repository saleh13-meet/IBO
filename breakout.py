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



for i in range(0,2):
	for j in range(0,10):
		bricks.append(Brick(x=(j)*brick_width*21,y=(i)*brick_height*-32,width=brick_width,height=brick_height,color=random.choice(colors)))

myball = Ball(x=0,y=0,dx=5,dy=-5,radius=1,color='red')
paddle = Brick(x=0,y=-SCREEN_HEIGHT+20,width=3,height=1,color=random.choice(colors))

def check_ball_collide(myball,brick):
	if(myball.right_side() >= brick.left_side()
	 	and myball.left_side() <= brick.right_side()
	 	and myball.top_side() >= brick.bottom_side()
	 	and myball.bottom_side() <= brick.top_side()):
		if(myball.xcor() in range(brick.left_side(), brick.right_side())):
			myball.dx = -myball.dx
			brick.hideturtle()
			if(brick in bricks):
				bricks.remove(brick)
		if(myball.ycor() in range(brick.bottom_side(),brick.top_side())):
			myball.dy = -myball.dy
			brick.hideturtle()
			if(brick in bricks):
				bricks.remove(brick)
 
while True:
	for brick in bricks:
		check_ball_collide(myball,paddle)
	if(myball.ycor()+ myball.radius> SCREEN_HEIGHT or myball.ycor() - myball.radius < -SCREEN_HEIGHT):
		myball.dy = -myball.dy
	if(myball.xcor()+ myball.radius> SCREEN_WIDTH or myball.xcor() - myball.radius < -SCREEN_WIDTH):
		myball.dx = -myball.dx

	myball.move()
	print(SCREEN_WIDTH, SCREEN_HEIGHT)
	getscreen().update()
	hideturtle()
mainloop()