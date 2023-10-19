import json
import math
import sys
from os import environ

environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


def draw_inclined_cylinder(
        radius: float = 1.0,
        height: float = 1.0,
        shift: tuple = (1.0, 1.0),
        sides: int = 100) -> None:
    shift_x = shift[0] / 2.0
    shift_y = shift[1] / 2.0
    angle_step = 360 / sides

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0 - shift_x, 0.0 - shift_y, -height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x1 = radius * math.cos(math.radians(angle)) - shift_x
        y1 = radius * math.sin(math.radians(angle)) - shift_y
        glVertex3f(x1, y1, -height / 2.0)
    glEnd()

    glBegin(GL_TRIANGLE_FAN)
    glVertex3f(0.0 + shift_x, 0.0 + shift_y, height / 2.0)
    for i in range(sides + 1):
        angle = i * angle_step
        x2 = radius * math.cos(math.radians(angle)) + shift_x
        y2 = radius * math.sin(math.radians(angle)) + shift_y
        glVertex3f(x2, y2, height / 2.0)
    glEnd()

    glBegin(GL_TRIANGLE_STRIP)
    for i in range(sides + 1):
        angle = i * angle_step
        x1 = radius * math.cos(math.radians(angle)) - shift_x
        y1 = radius * math.sin(math.radians(angle)) - shift_y
        x2 = radius * math.cos(math.radians(angle)) + shift_x
        y2 = radius * math.sin(math.radians(angle)) + shift_y
        glVertex3f(x1, y1, -height / 2.0)
        glVertex3f(x2, y2, height / 2.0)
    glEnd()


def start_render(appsettings_path: str = None):
    if appsettings_path is None:
        radius = 1.0
        height = 1.0
        shift = (1.0, 1.0)
        sides = 100
        color = [1.0, 0, 0, 1.0]
    else:
        with open(appsettings_path, encoding='UTF-8') as app_s:
            appsettings = json.load(app_s)
        radius = appsettings['radius']
        height = appsettings['height']
        shift = tuple(appsettings['shift'])
        sides = appsettings['sides']
        color = appsettings['color']
    flag = True

    pygame.init()
    display = (720, 720)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5.0)

    glEnable(GL_LIGHTING)
    glEnable(GL_DEPTH_TEST)

    glMaterial(GL_FRONT, GL_DIFFUSE, color)

    light_position = [0, 1, 0, 3]
    rotation_delta = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rotation_delta = 1
                elif event.key == pygame.K_RIGHT:
                    rotation_delta = -1
                elif event.key == pygame.K_w:
                    light_position[2] += 0.2
                elif event.key == pygame.K_a:
                    light_position[3] -= 0.2
                elif event.key == pygame.K_s:
                    light_position[2] -= 0.2
                elif event.key == pygame.K_d:
                    light_position[3] += 0.2
            elif event.type == pygame.KEYUP:
                if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                    rotation_delta = 0

        if flag:
            glRotatef(110, 1, 0, 0)
            flag = False

        glRotatef(rotation_delta, 1, 0, 0)

        glLightfv(GL_LIGHT0, GL_POSITION, light_position)
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 0.2])
        glEnable(GL_LIGHT0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        draw_inclined_cylinder(radius, height, shift, sides)
        pygame.display.flip()
        pygame.time.wait(10)


if __name__ == '__main__':
    try:
        if len(sys.argv) > 1:
            start_render(sys.argv[1])
        else:
            start_render()

    except OSError:
        print('OSError: could not open settings file!')
    except json.decoder.JSONDecodeError:
        print('JSONDecodeError: settings file is empty!')
