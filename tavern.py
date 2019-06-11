from pygame import *
from Options import *
import sys

START_POINT = 0
COST = 100


class Tavern(object):
    def __init__(self, positions):
        self.positions = positions

    def render(self, window, font, num_option):
        for i in self.positions:
            if num_option == i[5]:
                window.blit(font.render(i[2], 1, i[4]), (i[0], i[1]))
            else:
                window.blit(font.render(i[2], 1, i[3]), (i[0], i[1]))

    def start_tavern(self, window, bg_win, amount_of_coins, amount_of_health):
        """ЗАпуск меню"""

        font_menu = font.SysFont("Algerian,", 64)
        option = 0

        font.init()
        my_health = font.SysFont("Algerian", 48)
        my_coins = font.SysFont("Algerian", 48)
        cost = font.SysFont("Algerian", 36)

        key.set_repeat(1000, 1)
        mouse.set_visible(True)
        bg_box1 = image.load("bg_box1.png")
        bg_box2 = image.load("bg_box1.png")
        gold = image.load("gold.png")
        gold_c = image.load("gold.png")
        heart = image.load("heart.png")
        bg_decor1 = image.load("bg_tavern_decor1.png")
        bg_decor2 = image.load("bg_tavern_decor2.png")

        while True:

            window.blit(bg_win, (START_POINT, START_POINT))
            window.blit(bg_box1, (20, 100))
            window.blit(bg_box2, (20, 410))
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
                        return amount_of_health, amount_of_coins
                    if i.key == K_UP or i.key == K_w:
                        if option > 0:
                            option -= 1
                    if i.key == K_DOWN or i.key == K_s:
                        if option < len(self.positions) - 1:
                            option += 1
                    if i.key == K_RETURN:
                        if option == 1:
                            return amount_of_health, amount_of_coins
                        if option == 0:
                            if amount_of_coins >= COST:
                                amount_of_health += 1
                                amount_of_coins -= COST
                if i.type == MOUSEBUTTONDOWN and i.button == 1:
                    if option == 1:
                        return amount_of_health, amount_of_coins
                    elif option == 0:
                        if amount_of_coins >= COST:
                            amount_of_health += 1
                            amount_of_coins -= COST

            window.blit(bg_decor1, (220, 0))
            window.blit(bg_decor2, (400, 260))
            window.blit(gold, (420, 120))
            window.blit(heart, (420, 200))
            window.blit(gold_c, (90, 260))
            window.blit(my_coins.render(str(amount_of_coins), 1, (104, 142, 35)), (470, 120))
            window.blit(my_health.render(str(amount_of_health), 1, (86, 3, 25)), (470, 200))
            window.blit(cost.render(u"Cost: 100", 1, (104, 142, 35)), (150, 260))

            display.flip()
