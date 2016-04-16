# Illuminati BreakOut 420 Blaze It 360 No Scope REKT Best Game Ever Created By MEET Students.
# doritos.gif -> 100 x 144
# mountain_dew.gif -> 100 x 164

from breakout import *
import turtle



left = -width / 2 + 30
right = width / 2
bottom = -height / 2
top = height / 2

bricks = []

bricks_types = [Doritos, MountainDew]

border_spacing = [40, 50]
bricks_spacing = 5

platform = Platform(0, bottom + 20)
balls = [Ball(0,0, random.randint(-10**2, 10**2)/(10.0**2), -random.randint(0,10**2)/(10.0**2), 10, "red")]

platform_dx = 30
def Left():
	platform.Move(-platform_dx)
def Right():
	platform.Move(platform_dx)
def SetMousePosition():
	platform.Move(mouse_position()[0])

onkey(Left, "Left")
onkey(Right, "Right")

for x in range(left + border_spacing[0], right - border_spacing[0], doritos_size[0] + bricks_spacing):
	for y in range(top - border_spacing[1], 0, -(mountain_dew_size[1] + bricks_spacing)):
		a = random.randint(0, 1)
		bricks.append(bricks_types[a](x, y, a + 1))

colors = ["green", "blue", "purple", "pink", "orange", "brown"]

bricks.append(platform)
listen()

total_bricks = len(bricks)

while True:
	for ball in balls:
		ball.move()
		ball.Borders(left, right - 15, top - 25, bottom)
		ball.HitBricks(bricks)
		if len(balls) / float(total_bricks) / 4.0 % 1 == 0:
			print "ANOTHER BALL " - len(balls) + 1
			color = random.choice(colors)
			colors.remove(color)
			balls.append(Ball(-width + 50,0, random.randint(0.1, 0.5), -random.randint(0.1, 0.5), color))
	update()

mainloop()
