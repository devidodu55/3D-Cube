import pygame
from OpenGL.GL import *
from OpenGL.GLU import *

COULEURS = (
    (1, 0, 0),
    (0, 1, 0),
    (0, 0, 1),
    (1, 1, 0),
    (1, 0, 1),
    (0, 1, 1),
)

SOMMETS = (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1), 
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )

ARETES = (
    (0,1),
    (0,3),
    (0,4),
    (2,1),
    (2,3),
    (2,7),
    (6,3),
    (6,4),
    (6,7),
    (5,1),
    (5,4),
    (5,7)
    )

SURFACES = (
    (0, 1, 2, 3),
    (3, 2, 7, 6),
    (6, 7, 5, 4),
    (4, 5, 1, 0),
    (1, 5, 7, 2),
    (4, 0, 3, 6)
)

def Cube():
    glBegin(GL_QUADS)
    for i, surface in enumerate(SURFACES):
        glColor3fv(COULEURS[i])
        for vertex in surface:
            glVertex3fv(SOMMETS[vertex])
    glEnd()

    glBegin(GL_LINES)
    for edge in ARETES:
        for vertex in edge:
            glVertex3fv(SOMMETS[vertex])
    glEnd()

pygame.init()
ZONE = (800,800)
pygame.display.set_mode(ZONE, pygame.DOUBLEBUF|pygame.OPENGL)

gluPerspective(45, (ZONE[0]/ZONE[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glRotatef(1, 3, 1, 3)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    Cube()
    pygame.display.flip()
    pygame.time.wait(10)
