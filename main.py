import threading
import pygame
from pygame.locals import DOUBLEBUF, OPENGL
from OpenGL.GL import *
from OpenGL.GLU import *
import config
import simulation
import gui

def initialize_pygame():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    pygame.display.set_caption("Solar System Simulation")
    gluPerspective(45, (display[0] / display[1]), 0.1, 200.0)
    glTranslatef(0.0, 0.0, -100)

    glEnable(GL_DEPTH_TEST)

def run():
    initialize_pygame()

    gui_thread = threading.Thread(target=gui.run_gui)
    gui_thread.daemon = True
    gui_thread.start()

    simulation.run_simulation()

    while config.simulationRunning:
        pass

if __name__ == "__main__":
    run()
