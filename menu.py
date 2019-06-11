from pygame import *
from Options import *
import sys

START_POINT = 0


class Menu(object):
    def __init__(self, positions):
        self.positions = positions

    def render(self, window, font, num_option):
        for i in self.positions:
            if num_option == i[5]:
                window.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                window.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def start_menu(self, window, bg_win):
        """ЗАпуск меню"""

        init()
        """Звуки"""
        mixer.pre_init(44100, -16, 1, 512)
        mixer.init()
        music_menu = "menu.ogg"
        track_menu = mixer.Sound(music_menu)
        track_menu.play(-1)

        flag = True
        font_menu = font.SysFont("Algerian,", 64)
        option = 0

        key.set_repeat(1000, 1)
        mouse.set_visible(True)
        bg_menu_1 = image.load("bg_menu_1.png")
        bg_menu_2 = image.load("bg_menu_2.png")
        bg_menu_3 = image.load("bg_menu_3.png")
        bg_box1 = image.load("bg_box1.png")
        bg_box2 = image.load("bg_box1.png")
        bg_box3 = image.load("bg_box1.png")

        while flag:

            track_menu.play(-1)
            window.blit(bg_win, (START_POINT, START_POINT))
            window.blit(bg_menu_1, (630, 10))
            window.blit(bg_menu_2, (-70, 300))
            window.blit(bg_menu_3, (510, 380))
            window.blit(bg_box1, (215, 50))
            window.blit(bg_box2, (215, 240))
            window.blit(bg_box3, (215, 430))
            map = mouse.get_pos()
            for i in self.positions:
                if (map[0] > i[0] - 100 and map[0] < i[0] + 250 and
                        map[1] > i[1] - 50 and map[1] < i[1] + 90):
                    option = i[5]
                self.render(window, font_menu, option)

            for i in event.get():
                if i.type == QUIT:
                    sys.exit()
                if i.type == KEYDOWN:
                    if i.key == K_ESCAPE:
                        sys.exit()
                    if i.key == K_UP or i.key == K_w:
                        if option > 0:
                            option -= 1
                    if i.key == K_DOWN or i.key == K_s:
                        if option < len(self.positions) - 1:
                            option += 1
                    if i.key == K_RETURN:
                        if option == 0:
                            track_menu.stop()
                            flag = False
                        if option == 1:
                            num = Options()
                            num.start_options(window, bg_win)
                        if option == 2:
                            track_menu.stop()
                            sys.exit()
                if i.type == MOUSEBUTTONDOWN and i.button == 1:
                    track_menu.stop()
                    if option == 0:
                        flag = False
                    elif option == 1:
                        num = Options()
                        num.start_options(window, bg_win)
                    elif option == 2:
                        sys.exit()

            display.flip()
