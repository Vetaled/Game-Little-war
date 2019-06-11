from pygame import *
import sys


class Options(object):
    def __init__(self):
        print("")

    def start_options(self, window, bg_win):
        START_POINT = 0

        bg_op = image.load("bg_op.png")

        font.init()
        headline = font.SysFont("Algerian", 64)
        text1 = font.SysFont("MS PGothic", 32)
        text2 = font.SysFont("MS PGothic", 32)
        text3 = font.SysFont("MS PGothic", 32)
        text4 = font.SysFont("MS PGothic", 32)
        text5 = font.SysFont("MS PGothic", 32)
        text6 = font.SysFont("MS PGothic", 32)
        text7 = font.SysFont("MS PGothic", 32)

        flag = True
        while flag:

            for i in event.get():
                if i.type == QUIT:
                    sys.exit()
                if i.type == KEYDOWN:
                    if i.key == K_ESCAPE:
                        flag = False

            window.blit(bg_win, (START_POINT, START_POINT))
            window.blit(bg_op, (10, 300))
            window.blit(headline.render(u"Manual", 1, (104, 142, 35)), (300, 15))
            window.blit(text1.render(u"You play as a knight who must defend the Tower.", 1, (104, 142, 35)), (180, 120))
            window.blit(text2.render(u"Initially, the tower has 3hp, but you can buy them", 1, (104, 142, 35)),
                        (180, 170))
            window.blit(text3.render(u"in a tavern for 100 coins. Zombs from another", 1, (104, 142, 35)), (190, 220))
            window.blit(text4.render(u"side will attack the tower. Your task is to destroy", 1, (104, 142, 35)),
                        (180, 270))
            window.blit(text5.render(u"the zombs and. Arrows you can take in the Tower.", 1, (104, 142, 35)),
                        (180, 320))
            window.blit(text6.render(u"For each zombs knocked down you ", 1, (104, 142, 35)),
                        (350, 370))
            window.blit(text7.render(u" will be given 10 coins.", 1, (104, 142, 35)),
                        (380, 420))

            display.flip()
