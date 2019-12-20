
from command import Command
from settings import Settings

import pygame as pg

class DrawCommand(Command):

    def __init__(self):
        Command.__init__(self)
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))
        self.notify_observers()

    def execute(self, screen):
        for point in self.points:
            x, y = point
            pg.draw.circle(screen, Settings.DRAW_COLOR, (x, y), Settings.DRAW_STROKE)