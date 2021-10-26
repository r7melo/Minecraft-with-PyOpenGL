from app import App

from OpenGL.GL import *
from OpenGL.GLU import *



vertices = (
	(1, 0, 0),
	(1, 1, 0),
	(0, 1, 0),
	(0, 0, 0),
	(1, 0, 1),
	(1, 1, 1),
	(0, 0, 1),
	(0, 1, 1)
)

edges = (
	(0, 1),
	(0, 3),
	(0, 4),
	(2, 1),
	(2, 3),
	(2, 7),
	(6, 3),
	(6, 4),
	(6, 7),
	(5, 1),
	(5, 4),
	(5, 7)
)

class Cube:
	def __init__(self, tX, tY, tZ):
		glBegin(GL_LINES)
		for edge in edges:
			for vertex in edge:
				glVertex3f(vertices[vertex][0] + tX, vertices[vertex][1] + tY, vertices[vertex][2] + tZ)
		glEnd()



class CubesOnSpace:
	def update(self):
		for x in range(20):
			for z in range(20):
				Cube(x, 0, z)

class CubesOnSpace2:
	def update(self):
		for x in range(20):
			for z in range(20):
				Cube(x, 5, z)




if __name__=="__main__":
	app = App()
	cubes_on_space = CubesOnSpace()
	cubes_on_space2 = CubesOnSpace2()
	app.render.append(cubes_on_space)
	app.render.append(cubes_on_space)
	app.run()