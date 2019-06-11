from pygame import *
from menu import *
from tavern import *
from class_list import *
from iintersect import *
from death import *
from random import randrange

init()


class Animation(object):

    def __init__(self, sprites_r=None, sprites_u=None, sprites_d=None, timer=120):
        self.sprites_r = sprites_r
        self.sprites_u = sprites_u
        self.sprites_d = sprites_d
        self.time = timer
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0

    def update_r(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites_r):
                self.frame = 0

    def update_u(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites_u):
                self.frame = 0

    def update_d(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites_u):
                self.frame = 0

    def static(self):
        return self.sprites_r[0]

    def get_sprite_r(self):
        return self.sprites_r[self.frame]

    def get_sprite_d(self):
        return self.sprites_d[self.frame]

    def get_sprite_u(self):
        return self.sprites_u[self.frame]


class Zomb(object):

    def __init__(self, x_zomb, y_zomb, sprites_r=None, timer=100):
        self.sprites_r = sprites_r
        self.time = timer
        self.work_time = 0
        self.skip_frame = 0
        self.frame = 0
        self.check = False
        self.x_zomb = x_zomb
        self.y_zomb = y_zomb

    def update_r(self, dt):
        self.work_time += dt
        self.skip_frame = self.work_time // self.time
        if self.skip_frame > 0:
            self.work_time = self.work_time % self.time
            self.frame += self.skip_frame
            if self.frame >= len(self.sprites_r):
                self.frame = 0

    def get_sprite_r(self):
        return self.sprites_r[self.frame]

    def static(self):
        return self.sprites_r[0]


"""Константы"""
START_POINT = 0

ARROW_ST_X = 250
ARROW_ST_Y = 20

X_TOWER = -5
Y_TOWER = 230

X_TAVERN = 20
Y_TAVERN = 10

LENGTH_SCREEN_TOWN = 250
WIDTH_SCREEN_TOWN = 600

LENGTH_SCREEN_FIELD = 550
WIDTH_SCREEN_FIELD = 600

LENGTH_WINDOW = 800
WIDTH_WINDOW = 660

LENGTH_INFO = 800
WIDTH_INFO = 60

"""Звуки"""
mixer.pre_init(44100, -16, 1, 512)
mixer.init()
music_battle = "battle.ogg"
sound_hit = "hit.ogg"
track_battle = mixer.Sound(music_battle)
track_hit = mixer.Sound(sound_hit)

"""Текстуры"""
bg_arrow_static = image.load("Arrow1.png")
bg_grass = image.load("bg_grass2.png")
bg_pergament = image.load("bg_pergament.png")
bg_town = image.load("bg_town.png")
tower = image.load("tower.png")
gold = image.load("gold.png")
heart = image.load("heart.png")
bg_win = image.load("bg_win.png")
bg_tavern = image.load("bg_tavern.png")
bg_died = image.load("bg_died.png")
backgrownd = image.load("Back.png")
bg_arrow = "Arrow2.png"

"""Создание игроовой поеверхности"""
window = display.set_mode((LENGTH_WINDOW, WIDTH_WINDOW))
display.set_caption("Last Warrior")

town = Surface((LENGTH_SCREEN_TOWN, WIDTH_SCREEN_TOWN))
field = Surface((LENGTH_SCREEN_FIELD, WIDTH_SCREEN_FIELD))

info_string = Surface((LENGTH_INFO, WIDTH_INFO))

"""Создание меню"""
positions = [(300, 100, u"Start", (250, 250, 30), (128, 0, 0), 0),
             (330, 290, u"Info", (250, 250, 30), (128, 0, 0), 1),
             (330, 490, u"Quit", (250, 250, 30), (128, 0, 0), 2)]

menu = Menu(positions)
menu.start_menu(window, bg_win)

"""Создание таверны"""
tavern_option = [(105, 150, u"HP +1", (250, 250, 30), (128, 0, 0), 0),
                 (105, 460, u"Back", (250, 250, 30), (128, 0, 0), 1)]
tavern_menu = Tavern(tavern_option)

"""Задание текстур персоонажа"""
sprite_z = image.load("zomb.png").convert_alpha()
sprite_h_r = image.load("hero.png").convert_alpha()
sprite_h_u = image.load("hero_u.png").convert_alpha()
sprite_h_d = image.load("hero_d.png").convert_alpha()

"""Создание текстовых переменных"""
font.init()
health = font.SysFont("Algerian", 32)
coins = font.SysFont("Algerian", 32)
tavern = font.SysFont("Algerian", 28)
tavern_f = font.SysFont("Algerian", 16)
arrow = font.SysFont("Algerian", 32)
press_e = font.SysFont("Algerian", 32)

"""Создание стерл, выпускаемых героем"""
x_arrow = -100
y_arrow = 0
arr = Object(x_arrow, ARROW_ST_Y, bg_arrow)
arr1 = Object(x_arrow, ARROW_ST_Y, bg_arrow)
arr2 = Object(x_arrow, ARROW_ST_Y, bg_arrow)
arr3 = Object(x_arrow, ARROW_ST_Y, bg_arrow)
counter_tower = 15
counter_hero = 0

"""Создание зомби"""
anim_z = []
anim_z.append(sprite_z.subsurface((0, 0, 31, 48)))
anim_z.append(sprite_z.subsurface((31, 0, 31, 48)))
anim_z.append(sprite_z.subsurface((62, 0, 31, 48)))
anim_z.append(sprite_z.subsurface(95, 0, 31, 48))

x_zomb = 860
y_zomb = None

timer_z = 240
AMOUNT_OF_ZOMB = 15
zombs = []
zomb = None
speed = 0
zomb_on_the_field = 0

for i in range(10):
    x_zomb = 860
    y_zomb = 60
    zombarik = Zomb(x_zomb, y_zomb + i * 60, anim_z, timer_z)
    zombs.append(zombarik)

"""Создание анимированного ГЕРОЯ"""
anim_h_r = []
anim_h_r.append(sprite_h_r.subsurface((0, 0, 33, 48)))
anim_h_r.append(sprite_h_r.subsurface((33, 0, 33, 48)))
anim_h_r.append(sprite_h_r.subsurface((66, 0, 33, 48)))
anim_h_r.append(sprite_h_r.subsurface(99, 0, 29, 48))

anim_h_u = []
anim_h_u.append(sprite_h_u.subsurface((0, 0, 33, 48)))
anim_h_u.append(sprite_h_u.subsurface((33, 0, 33, 48)))
anim_h_u.append(sprite_h_u.subsurface((66, 0, 33, 48)))
anim_h_u.append(sprite_h_u.subsurface(99, 0, 29, 48))

anim_h_d = []
anim_h_d.append(sprite_h_d.subsurface((0, 0, 33, 48)))
anim_h_d.append(sprite_h_d.subsurface((33, 0, 33, 48)))
anim_h_d.append(sprite_h_d.subsurface((66, 0, 33, 48)))
anim_h_d.append(sprite_h_d.subsurface(99, 0, 29, 48))

speed_of_hero = 1
x_hero = 50
y_hero = 300
hero_flag = True

timer = 240
hero = Animation(anim_h_r, anim_h_u, anim_h_d, timer)

"""Задание переменных отвечающих за жизни и деньги"""
amount_of_health = 3
amount_of_coins = 100

#"""Создание анимированного КОЛХОЗНИКА"""
#sprite_k = image.load("krest.png").convert_alpha()
#anim_k = []

"""Таймер"""
clock = time.Clock()
dt = 0

"""Cмерть"""
die = Died()

"""Скорость отклика"""
key.set_repeat(100, 1)

"""Запуск игры"""

flag = True
while flag:

    track_battle.play(-1)

    """Закраска игровых полей Город, Поле, Информационная строка"""
    town.fill((100, 100, 100))
    field.fill((50, 70, 100))
    info_string.fill((170, 170, 170))

    """Вывод на экран полей Город, Поле, Информационная строка"""
    field.blit(bg_grass, (START_POINT, START_POINT))
    info_string.blit(bg_pergament, (START_POINT, START_POINT))

    info_string.blit(bg_tavern, (X_TAVERN, Y_TAVERN))
    info_string.blit(bg_arrow_static, (ARROW_ST_X, ARROW_ST_Y))
    info_string.blit(gold, (620, 10))
    info_string.blit(heart, (450, 12))
    info_string.blit(arrow.render(str(counter_hero), 1, (0, 0, 35)), (330, 12))
    info_string.blit(coins.render(str(amount_of_coins), 1, (104, 142, 35)), (670, 15))
    info_string.blit(health.render(str(amount_of_health), 1, (86, 3, 25)), (500, 15))
    info_string.blit(tavern.render(u"Taverna", 1, (128, 0, 0)), (60, 5))
    info_string.blit(tavern_f.render(u"(press T)", 1, (128, 0, 0)), (80, 30))

    town.blit(bg_town, (START_POINT, START_POINT))
    town.blit(tower, (X_TOWER, Y_TOWER))
    if intersect(60, x_hero, 294, y_hero, 30, 30):
        town.blit(press_e.render(u"E", 1, (0, 0, 35)), (X_TOWER + 55, Y_TOWER + 5))

    ######
    """Обработка событий"""
    for i in event.get():
        if i.type == QUIT:
            flag = False
        if i.type == KEYDOWN:
            if i.key == K_e:
                key.set_repeat(150, 1)
                if intersect(60, x_hero, 294, y_hero, 30, 30):
                    if counter_hero < counter_tower:
                        counter_hero = 0
                        counter_hero += counter_tower
            if i.key == K_LEFT or i.key == K_a:
                if x_hero > START_POINT:
                    hero_flag = False
                    x_hero -= speed_of_hero
                    hero.update_r(dt)
                    town.blit(hero.get_sprite_r(), (x_hero, y_hero))
            if i.key == K_RIGHT or i.key == K_d:
                if x_hero < LENGTH_SCREEN_TOWN - 33:
                    hero_flag = False
                    x_hero += speed_of_hero
                    hero.update_r(dt)
                    town.blit(hero.get_sprite_r(), (x_hero, y_hero))
            if i.key == K_UP or i.key == K_w:
                if y_hero > START_POINT:
                    hero_flag = False
                    y_hero -= speed_of_hero
                    hero.update_u(dt)
                    town.blit(hero.get_sprite_u(), (x_hero, y_hero))
            if i.key == K_DOWN or i.key == K_s:
                if y_hero < WIDTH_SCREEN_TOWN - 48:
                    hero_flag = False
                    y_hero += speed_of_hero
                    hero.update_d(dt)
                    town.blit(hero.get_sprite_d(), (x_hero, y_hero))
            if i.key == K_ESCAPE:
                track_battle.stop()
                menu.start_menu(window, bg_win)
                key.set_repeat(100, 1)
            if i.key == K_t:
                amount_of_health, amount_of_coins = tavern_menu.start_tavern(window, bg_win, amount_of_coins,
                                                                             amount_of_health)
                key.set_repeat(100, 1)
            if i.key == K_SPACE:
                track_hit.play()
                if counter_hero > 0:
                    if not arr3.push and arr2.push:
                        arr3.x = x_hero + 10
                        arr3.y = y_hero + 60
                        arr3.push = True
                        counter_hero -= 1
                    if not arr2.push and arr1.push:
                        arr2.x = x_hero + 10
                        arr2.y = y_hero + 60
                        arr2.push = True
                        counter_hero -= 1
                    if not arr1.push and arr.push:
                        arr1.x = x_hero + 10
                        arr1.y = y_hero + 60
                        arr1.push = True
                        counter_hero -= 1
                    if not arr.push:
                        arr.x = x_hero + 10
                        arr.y = y_hero + 60
                        arr.push = True
                        counter_hero -= 1

    if arr.x > LENGTH_WINDOW:
        arr.push = False

    if not arr.push:
        arr.y = ARROW_ST_Y
        arr.x = -100
    else:
        arr.x += 5

    if arr1.x > LENGTH_WINDOW:
        arr1.push = False

    if not arr1.push:
        arr1.y = ARROW_ST_Y
        arr1.x = -100
    else:
        arr1.x += 5

    if arr2.x > LENGTH_WINDOW:
        arr2.push = False

    if not arr2.push:
        arr2.y = ARROW_ST_Y
        arr2.x = -100
    else:
        arr2.x += 5

    if arr3.x > LENGTH_WINDOW:
        arr3.push = False

    if not arr3.push:
        arr3.y = ARROW_ST_Y
        arr3.x = -100
    else:
        arr3.x += 5

    if hero_flag:
        town.blit(hero.static(), (x_hero, y_hero))
    hero_flag = True

    window.blit(town, (START_POINT, WIDTH_INFO))
    window.blit(field, (LENGTH_SCREEN_TOWN, WIDTH_INFO))
    window.blit(info_string, (START_POINT, START_POINT))

    for g in range(len(zombs)):
        zombs[g].check = True
        zombs[g].update_r(dt)
        window.blit(zombs[g].get_sprite_r(), (zombs[g].x_zomb, zombs[g].y_zomb))
        zomb_on_the_field += 1

    for j in range(len(zombs)):

        if amount_of_health <= 3:
            speed = 0.3
            speed_of_hero = 1
        if 3 < amount_of_health <= 5:
            speed = 0.5
            speed_of_hero = 1.2
        if 5 < amount_of_health <= 10:
            speed = 0.7
            speed_of_hero = 1.4
        if amount_of_health > 10:
            speed = 1.2
            speed_of_hero = 1.7

        if zombs[j].x_zomb < 0:
            zombs[j].check = False
            zomb_on_the_field -= 1
            amount_of_health -= 1

        if intersect(zombs[j].x_zomb, arr1.x, zombs[j].y_zomb + 17, arr1.y, 24, 24):
            amount_of_coins += 10
            zombs[j].check = False
            zomb_on_the_field -= 1
            arr1.x = 900
            arr1.y = 0
        if intersect(zombs[j].x_zomb, arr.x, zombs[j].y_zomb + 17, arr.y, 24, 24):
            amount_of_coins += 10
            zombs[j].check = False
            zomb_on_the_field -= 1
            arr.x = 900
            arr.y = 0
        if intersect(zombs[j].x_zomb, arr2.x, zombs[j].y_zomb + 17, arr2.y, 24, 24):
            amount_of_coins += 10
            zombs[j].check = False
            zomb_on_the_field -= 1
            arr2.x = 900
            arr2.y = 0
        if intersect(zombs[j].x_zomb, arr3.x, zombs[j].y_zomb + 17, arr3.y, 24, 24):
            amount_of_coins += 10
            zombs[j].check = False
            zomb_on_the_field -= 1
            arr3.x = 900
            arr3.y = 0

        if not zombs[j].check:
            zombs[j].x_zomb = x_zomb
            zombs[j].y_zomb = randrange(60, 600, 15)
        else:
            zombs[j].x_zomb -= speed

    if amount_of_health <= 0:
        track_battle.stop()
        die.start_deth(window)
        amount_of_health = 3
        amount_of_coins = 100
        counter_hero = 0
        for i in range(10):
            zombs[i].x_zomb = 860
            zombs[i].y_zomb = 60 + i * 60

    arr.render(window)
    arr1.render(window)
    arr2.render(window)
    arr3.render(window)
    display.flip()

    dt = clock.tick(120)
