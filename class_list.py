from pygame import *


class Object(object):
    def __init__(self, obj_x, obj_y, filename):
        self.x = obj_x
        self.y = obj_y
        self.bitmpap = image.load(filename)
        self.bitmpap.set_colorkey((0, 0, 0))
        self.push = False

    def render(self, screen):
        screen.blit(self.bitmpap, (self.x, self.y))
