# Marching Cubes Algorithm
import matrix as m # maths (mainly trigonometry)
from Cube import Cube

'''
IMPORTANT NOTE:

could implement some parts of this the the matrix module ...

'''

def generate_world(width, height, depth, cube_size):

	# generate a 3-dimensional matrix filled with Cube-objects
	world = [[[Cube((-(width/2 * cube_size) + x * cube_size,
					 -(height/2 * cube_size) + y * cube_size,
					 -(depth/2 * cube_size) + z * cube_size),
					 cube_size) for x in range(width)] for y in range(height)] for z in range(depth)]

	# if width == height == depth:
	# 	x = width * cube_size / 2
	# 	y = width * cube_size / 2
	# 	z = width * cube_size / 2

	# 	box = Cube((x,y,z), width * cube_size / 2)
	# 	box.vertex_color = (0,1,0)

	# else:
	# 	box = None

	# return the matrix
	return world # , box


def apply_to_world(world, function):

	# run through all Cubes in the wold
	for stage in world:
		for line in stage:
			for cube in line:
				cube.inside = []
				# iterate through all vertex
				for x,vertex in enumerate(cube.vertices):
					# if function, add the vertex to the 'inside' of the shape
					if function(vertex[0],vertex[1],vertex[2]):
						# print('apended {}'.format(x))
						cube.inside.append(x)
				cube.set_triangles()


def draw_world(world):

	# run through all Cubes in the wold
	for stage in world:
		for line in stage:
			for cube in line:
				cube.draw()


def world_iteration(world):
	for stage in world:
		for line in stage:
			for cube in line:
				yield cube

