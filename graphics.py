# OpengGL related functions
from OpenGL.GL import * # opengl basics
from OpenGL.GLU import * # opengl advanced
from pygame_module import color # rgb-color dictionnary
from matrix import vector

# opengl-rgb is from 0 to 1, not from 0 to 255
rgb_to_opengl = lambda rgb : [value / 255 for value in rgb]

'''
opengl coordinates :
X : from left '-' to right '+'
Y : from down '-' ro up '+'
Z : from far '-' to near '+'
'''

'''
 - verticies :

   4--------5
  /|       /|
 / |      / |
7--------6  |
|  0-----|--1
| /      | /
|/       |/
3--------2


 - edge_points :

    ----4-----
   /|       /|
  7 8      5 9
 /  |     /  |
-----6----   |
|  '---0-|---'
11 /     10 /
| 3      | 1
|/       |/
-----2----


'''


# vertices (or nodes) in a cube
vertices = (
		 (-1,-1,-1), # 0
		 (1,-1,-1),  # 1
		 (1,-1,1),   # 2
		 (-1,-1,1),  # .
		 (-1,1,-1),  # .
		 (1,1,-1),   # .
		 (1,1,1),
		 (-1,1,1)
		 )

# connections (by index) of the vertices
edges = ((0,1),(0,3),(0,4),(2,1),(2,3),(2,6),(7,3),(7,4),(7,6),(5,1),(5,4),(5,6))

# edge-points of a cube
edge_points = (
		 (0,-1,-1),  # 0
		 (1,-1,0),   # 1
		 (0,-1,1),   # 2
		 (-1,-1,0),  # .

		 (0,1,-1),   # .
		 (1,1,0),    # .
		 (0,1,1),
		 (-1,1,0),

		 (-1,0,-1),
		 (1,0,-1),
		 (1,0,1),
		 (-1,0,1)
		 )

# - functions -
def set_vertices(translation_vector):
	""" Returns new vertices by a translation_vector.
	The translation_vector is formed by (x_change,y_change,z_change)
	"""

	new_vertices = [vector.add(vertex, translation_vector) for vertex in vertices]

	return new_vertices


def set_edge_points(translation_vector):
	""" Returns new edge_points by a translation_vector.
	The translation_vector is formed by (x_change,y_change,z_change)
	"""

	new_edge_points = [vector.add(edge_point, translation_vector) for edge_point in edge_points]

	return new_edge_points


def resize_vertices(vertices, size):
	""" Returns new vertices, by a given size """
	
	ratio = size/2 # normal size is 2

	new_vertices = [vector.multiplication_k(vertex, ratio) for vertex in vertices]

	return new_vertices


def resize_edge_points(edge_points, size):
	""" Returns new edge_points, by a given size """
	
	ratio = size/2 # normal size is 2

	new_edge_points = [vector.multiplication_k(edge_point, ratio) for edge_point in edge_points]

	return new_edge_points

