from pygame import *
import sys

bg_died = image.load("bg_died.png")
backgrownd = image.load("Back.png")


class Died(object):
    def __init__(self):
        self.back = backgrownd
        self.died = bg_died

    def start_deth(self, window):

        init()
        mixer.pre_init(44100, -16, 1, 512)
        mixer.init()
        music_death = "death.ogg"
        mixer.music.set_volume(0.5)
        track_death = mixer.Sound(music_death)

        flag = True
        while flag:
            track_death.play(-1)
            window.blit(self.back, (0, 0))
            window.blit(self.died, (300, -40))
            for i in event.get():
                if i.type == QUIT:
                    sys.exit()
                if i.type == KEYDOWN:
                    if i.key == K_ESCAPE:
                        track_death.stop()
                        return 0
            display.flip()
