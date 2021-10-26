import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from threading import Thread 

vertices = (
	(1, -1, -1),
	(1, 1, -1),
	(-1, 1, -1),
	(-1, -1, -1),
	(1, -1, 1),
	(1, 1, 1),
	(-1, -1, 1),
	(-1, 1, 1)
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

pygame.init()

screenSize = (600, 600)
pygame.display.set_mode(screenSize, DOUBLEBUF | OPENGL)

clock = pygame.time.Clock()

glMatrixMode(GL_PROJECTION)
gluPerspective(45, (screenSize[0] / screenSize[1]), 0.1, 50.0)
glMatrixMode(GL_MODELVIEW)
glTranslate(0, -3, -30)

current_mv_mat = (GLfloat * 16)()



glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
glLoadIdentity()

glMultMatrixf(current_mv_mat)


glPushMatrix()

glGetFloatv(GL_MODELVIEW_MATRIX, current_mv_mat)
glLoadIdentity()
glRotatef(0, 1, 0, 0)
glMultMatrixf(current_mv_mat)

def teste():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    for i in range(8):
        for j in range(8):
            glBegin(GL_LINES)
            for edge in edges:
                for vertex in edge:
                    glVertex3f(vertices[vertex][0] + i, vertices[vertex][1], vertices[vertex][2] + j)
            glEnd()

    glPopMatrix()

t = Thread(target=teste)
t.start()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_ESCAPE]:
        pygame.quit()
        quit()

    pygame.display.flip()
    clock.tick(60)
    
