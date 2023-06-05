import pygame
import sys
from pygame.math import Vector2 as vector
from pygame.mouse import get_pressed as mouse_buttons
from pygame.mouse import get_pos as mouse_pos
from settings import *


class Editor:
    def __init__(self):
        # main setup
        self.display_surface = pygame.display.get_surface()

        # navigation
        self.origin = vector()
        self.pan_active = False

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            self.pan_input(event)

    def pan_input(self, event):

        # middle mouse button pressed / released
        if event.type == pygame.MOUSEBUTTONDOWN and mouse_buttons()[1]:
            self.pan_active = True
        if not mouse_buttons()[1]:
            self.pan_active = False

        # panning update
        if self.pan_active:
            self.origin = mouse_pos()

    def run(self, dt):
        self.display_surface.fill('white')
        self.event_loop()
        pygame.draw.circle(self.display_surface, 'red', self.origin, 10)
