import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import config
from planets import celestial_bodies

def draw_sphere(radius, slices, stacks):
    quad = gluNewQuadric()
    gluSphere(quad, radius, slices, stacks)

def draw_solar_system():
    with config.lock:
        local_time_multiplier = config.time_multiplier

    for P_object in celestial_bodies:
        glPushMatrix()
        P_object.angle += P_object.orbit_speed * local_time_multiplier * 0.1
        glRotatef(P_object.angle % 360, 0, 1, 0)
        glTranslatef(P_object.distance, P_object.height, 0)  
        glColor3f(*P_object.color)  
        draw_sphere(P_object.radius, 32, 32)
        glPopMatrix()

def run_simulation():
    is_rotating = False
    is_moving = False
    last_mouse_x, last_mouse_y = 0, 0

    while config.simulationRunning:  # Run while the simulation is running

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                with config.lock:
                    config.simulationRunning = False  # Set to False when quitting
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                with config.lock:
                    if event.button == 4:  
                        camera_z = config.zoom_factor
                        glTranslatef(0.0, 0.0, config.zoom_factor)
                    elif event.button == 5:  
                        camera_z = -config.zoom_factor
                        glTranslatef(0.0, 0.0, -config.zoom_factor)
                    elif event.button == 3:  
                        is_rotating = True
                        last_mouse_x, last_mouse_y = pygame.mouse.get_pos()
                    elif event.button == 1:  
                        is_moving = True
                        last_mouse_x, last_mouse_y = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 3:  
                    is_rotating = False
                elif event.button == 1:  
                    is_moving = False

            if event.type == pygame.MOUSEMOTION:
                if is_rotating:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    dx = mouse_x - last_mouse_x
                    dy = mouse_y - last_mouse_y
                    config.rotation_x += dy * 0.2
                    config.rotation_y += dx * 0.2
                    last_mouse_x, last_mouse_y = mouse_x, mouse_y

                if is_moving:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    dx = mouse_x - last_mouse_x
                    dy = mouse_y - last_mouse_y
                    with config.lock:
                        glTranslatef(dx * config.camera_speed, -dy * config.camera_speed, 0)
                    last_mouse_x, last_mouse_y = mouse_x, mouse_y

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        glRotatef(config.rotation_x, 1, 0, 0)
        glRotatef(config.rotation_y, 0, 1, 0)

        draw_solar_system()
        glPopMatrix()

        pygame.display.flip()
        pygame.time.wait(10)
