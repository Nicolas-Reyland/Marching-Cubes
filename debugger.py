# Marching Cubes, World Debugger
from algorithm import world_iteration

world = None

def feed(world_input):
	global world
	world = world_input[:]

def interpreter(command):
	global world
	if command == '':
		return

	if command == 'shape':
		print('x {}, y {}, z {}'.format(len(world[0][0]), len(world[0]), len(world)))

	elif command == 'xyz min max':
		print('x min: {}, x max: {}'.format(world[0][0][0].pos[0], world[-1][-1][-1].pos[0]))
		print('y min: {}, y max: {}'.format(world[0][0][0].pos[1], world[-1][-1][-1].pos[1]))
		print('z min: {}, z max: {}'.format(world[0][0][0].pos[2], world[-1][-1][-1].pos[2]))

	elif command == 'all':
		for ci,cube in enumerate(list(world_iteration(world))):
			print('cube {} at {}'.format(ci,cube.pos))
			print('vertices :')
			for i,vertex in enumerate(cube.vertices):
				print('vertex {} at {}'.format(i,vertex))
			print('triangles :')
			for i,triangle in enumerate(cube.triangles):
				print('triangle {} at {}'.format(i,triangle))
			print()

	elif command == 'triangles':
		for cube in filter(lambda c: c.triangles,list(world_iteration(world))):
			print('cube at {}'.format(cube.pos))
			for triangle in cube.triangles:
				print(triangle)

	else:
		print('Invalid Command {} !'.format(command))


