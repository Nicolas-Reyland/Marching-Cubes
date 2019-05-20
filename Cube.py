# Cube Class - Marching Cubes Algorithm
from graphics import *
from triangles import get_triangles # triangle-table look-up

class Cube:

	""" - Cube Class -



	"""

	def __init__(self, pos, size, inside=[]):

		# coordinates
		self.pos = pos # center of the cube

		# shape
		self.size = size
		# vertices
		self.vertices = set_vertices(self.pos)
		self.vertices = resize_vertices(self.vertices, self.size)
		# edge_points
		self.edge_points = set_edge_points(self.pos)
		self.edge_points = resize_edge_points(self.edge_points, self.size)

		# initialization
		self.inside = inside
		self.triangles = []
		self.surface_color = rgb_to_opengl((230,35,35))
		self.vertex_color = rgb_to_opengl((255,255,255))

	def set_triangles(self):
		# make the list unique
		self.inside = list(set(self.inside))
		# print('inside is',self.inside)
		# fetch the triangles
		triangles = get_triangles(self.inside)
		# print('beginning:',triangles)
		# filter the -1s out
		triangles = triangles[:triangles.index(-1)]
		# print('middle:',triangles)
		# chunk into groups of 3 (nodes for 1 triangle is a group of 3 index')
		triangles = [triangles[i:i+3] for i in range(0,len(triangles),3)]
		# apply
		# print('finally:',triangles)
		self.triangles = triangles

	def draw(self):

		# surfaces
		for triangle in self.triangles:
			# glBegin(GL_TRIANGLES)
			for i in range(3):
				glColor3fv(self.surface_color)
				glVertex3fv(self.edge_points[triangle[i]])
			glColor3fv((1,1,1)) # color to white
			# glEnd()

	def raw_draw(self):

		# glBegin(GL_TRIANGLES)
		# glColor3fv(self.vertex_color)
		# glEnd()

		# vertices
		# glBegin(GL_LINES)
		for edge in edges: # from little_opengl
			glVertex3fv(self.vertices[edge[0]])
			glVertex3fv(self.vertices[edge[1]])
		# glEnd()

	def interpolate(self):
		pass
