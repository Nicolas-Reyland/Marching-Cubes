# Marching Cubes Algorithm
import pygame as pg # rendering
from graphics import * # opengl-related stuff
import algorithm # marching cubes algorithm

world_dimensions = (10,10,10)
world_cube_size = .25
world = algorithm.generate_world(world_dimensions[0],world_dimensions[1],world_dimensions[2], world_cube_size)

function_tolerance = 0


def function(x,y,z):
	global function_tolerance

	return y < 0


algorithm.apply_to_world(world, function)

from debugger import feed, interpreter




# ----- Graphics Main Loop -----
def main():

	global function_tolerance

	from os import system

	# start movement
	glTranslatef(0, 0, -world_dimensions[2] * world_cube_size * 1.5)

	# the camera rotation values
	camera_rot_x = 0
	camera_rot_y = 0

	camera_movm_x = 0
	camera_movm_y = 0

	# constants
	game_speed = 2
	direction_speed = .5

	# main loop
	while True:

		# input('input')

		# go through pg.events
		for event in pg.event.get():
			# if the window cross has been clicked, quit everything
			if event.type == pg.QUIT:
				# terminate pygame
				pg.quit()
				# terminate the program
				quit()

			# if the event-type is a key-pressed
			if event.type == pg.KEYDOWN:
				# 'q' terminates the program
				if event.key == pg.K_q:
					pg.quit()
					quit()

				# camera movement
				if event.key == pg.K_RIGHT:
					camera_movm_x = -direction_speed
				if event.key == pg.K_LEFT:
					camera_movm_x = direction_speed
				if event.key == pg.K_UP:
					camera_movm_y = -direction_speed
				if event.key == pg.K_DOWN:
					camera_movm_y = direction_speed

				# camera rotation
				if event.key == pg.K_j:
					camera_rot_x = -direction_speed

				if event.key == pg.K_l:
					camera_rot_x = direction_speed

				if event.key == pg.K_i:
					camera_rot_y = direction_speed

				if event.key == pg.K_k:
					camera_rot_y = -direction_speed

				# terminal screen clear
				if event.key == pg.K_c:
					system('clear')

				if event.key == pg.K_a:
					world[0][0][0].inside = list(map(int, input('inside: ').split(',')))
					world[0][0][0].set_triangles()
					for cube in list(algorithm.world_iteration(world)):
						print(cube)
						print(cube.pos, len(cube.triangles))
						if len(cube.triangles):
							for triangle in cube.triangles:
								print('triangle {}'.format([cube.edge_points[triangle[i]] for i in range(3)]))
						print()
					# cube.inside = list(map(int, input('inside: ').split(',')))
					# cube.set_triangles()

				if event.key == pg.K_w:
					function_tolerance += .01
					algorithm.apply_to_world(world, function)
					print('function tolerance set to {}'.format(function_tolerance))

				if event.key == pg.K_s:
					function_tolerance -= .01
					algorithm.apply_to_world(world, function)
					print('function tolerance set to {}'.format(function_tolerance))

				if event.key == pg.K_d:
					feed(world)
					interpreter(input('command: '))


			# Moving, etc.
			if event.type == pg.KEYUP:
				# camera
				if event.key == pg.K_j or event.key == pg.K_l:
					camera_rot_x = 0
				if event.key == pg.K_i or event.key == pg.K_k:
					camera_rot_y = 0
				if event.key == pg.K_RIGHT or event.key == pg.K_LEFT:
					camera_movm_x = 0
				if event.key == pg.K_UP or event.key == pg.K_DOWN:
					camera_movm_y = 0

			# the mouse-button-scrolling
			if event.type == pg.MOUSEBUTTONDOWN: # mouse-wheel

				if event.button == 4: # forward
					glTranslatef(0,0,direction_speed)
				if event.button == 5: # backwards
					glTranslatef(0,0,-direction_speed)

		# moving camera
		glTranslatef(camera_movm_x,camera_movm_y,0)
		# rotating camera
		glRotatef(10, camera_rot_y, camera_rot_x, 0)

		# clear frame : specify what we wanna clear
		glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

		### DRAWING HERE
		glBegin(GL_TRIANGLES)
		for cube in list(algorithm.world_iteration(world)):
					if cube.triangles:
						cube.draw()
		glEnd()
		# glBegin(GL_LINES)
		# for stage in world:
		# 	for line in stage:
		# 		for cube in line:
		# 			cube.raw_draw()
		# glEnd()
		# cube.draw()
		# box.raw_draw()

		# update the display
		pg.display.flip()

		# wait 100 ms
		# pg.time.wait(100)


# graphics initialization
pg.init()
WIDTH, HEIGHT = 1000, 800

screen = pg.display.set_mode((WIDTH, HEIGHT), pg.DOUBLEBUF|pg.OPENGL)

# enable strong colors
# glEnable(GL_DEPTH_TEST)

# init opengl
gluPerspective(45, WIDTH/HEIGHT, .1, 50)

if __name__ == '__main__':
	main()


