# Illuminati BreakOut 420 Blaze It 360 No Scope REKT Best Game Ever Created By MEET Students.
# doritos.gif -> 100 x 144
# mountain_dew.gif -> 100 x 164

from breakout import *
import turtle

def Left():
	platform.Move(-15)
def Right():
	platform.Move(15)

left = -width / 2 + 30
right = width / 2
bottom = -height / 2
top = height / 2

bricks = []

bricks_types = [Doritos, MountainDew]

border_spacing = [40, 50]
bricks_spacing = 5

platform = Platform(0, bottom)
ball = Ball(0,0, random.randint(-10**2, 10**2)/(10.0**2), -random.randint(0,10**2)/(10.0**2), 12, "red")

onkey(Left, "Left")
onkey(Right, "Right")


for x in range(left + border_spacing[0], right - border_spacing[0], doritos_size[0] + bricks_spacing):
	for y in range(top - border_spacing[1], 0, -(mountain_dew_size[1] + bricks_spacing)):
		a = random.randint(0, 1)
		bricks.append(bricks_types[a](x, y, a + 1))

listen()

while True:
	ball.move()
	ball.Borders(left, right - 15, top - 25, bottom)
	update()

mainloop()
