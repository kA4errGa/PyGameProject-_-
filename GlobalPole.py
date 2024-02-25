from pygame import *
import random


class GlobalPole:
    def __init__(self):
        self.coords = None
        self.local_list = random.sample(['Сумрачный лес', 'Сокровищница дракона', 'Большой город',
                                         'Логово чародея', 'Деревня', 'Хлебные поля', 'Эльфийское озеро'], 4)
        self.local_list.append('Player')
        self.local = {}
        self.pos_loced = []
        for i in range(5):
            self.what_pos()
            while self.coords in self.pos_loced:
                self.what_pos()
            self.this_pos(i)

    def what_pos(self):
        pos = random.randint(0, 63)
        a = pos // 8
        b = pos % 8
        self.coords = (b, a)

    def this_pos(self, ii):
        self.local[self.local_list[ii]] = self.coords
        self.pos_loced.append(self.coords)

    def paint_icon(self, s):
        for i in self.local:
            if i == 'Сумрачный лес' and self.local[i] != (-1, -1):
                s.blit(image.load('image/forest_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Сокровищница дракона':
                s.blit(image.load('image/dragon_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Большой город':
                s.blit(image.load('image/city_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Логово чародея':
                s.blit(image.load('image/wizard_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Деревня':
                s.blit(image.load('image/wilage_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Хлебные поля':
                s.blit(image.load('image/pole_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Эльфийское озеро':
                s.blit(image.load('image/elf_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))
            if i == 'Player':
                s.blit(image.load('image/player_icon.png'), (204 + self.local[i][0] * 62, 19 + self.local[i][1] * 72))

    def get_self_local(self):
        return self.local

    def player_up_y(self):
        self.pos_x = self.local['Player'][0]
        self.pos_y = self.local['Player'][1]
        self.local['Player'] = (self.pos_x, max(0, self.pos_y - 1))

    def player_down_y(self):
        self.pos_x = self.local['Player'][0]
        self.pos_y = self.local['Player'][1]
        self.local['Player'] = (self.pos_x, min(7, self.pos_y + 1))

    def player_up_x(self):
        self.pos_x = self.local['Player'][0]
        self.pos_y = self.local['Player'][1]
        self.local['Player'] = (min(self.pos_x + 1, 7), self.pos_y)

    def player_down_x(self):
        self.pos_x = self.local['Player'][0]
        self.pos_y = self.local['Player'][1]
        self.local['Player'] = (max(self.pos_x - 1, 0), self.pos_y)

    def player_take_ivent(self):
        for i in self.local:
            if i != 'Player' and self.local[i] == self.local['Player']:
                return i
        return False

    def del_ivent(self, ivent_name):
        self.local[ivent_name] = (-1, -1)
