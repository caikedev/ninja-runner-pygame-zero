import pgzrun

WIDTH= 800
HEIGHT= 600

def draw():
	screen.draw.filled_rect(Rect(0, 0, 800, 400), (163, 232, 254))
	screen.draw.filled_rect(Rect(0, 400, 800, 200), (88, 242, 152))

def update():
	if runner.image == 'run__000':
		runnerimage == 'run__001'
	elif runner.image == 'run__001':
		runner.image == 'run__002'
	elif runer.image == 'run__002':
		runner.image == 'run__000'

pgzrun.go()