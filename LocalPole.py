from pygame import *
import random


class LocalPole:
    def __init__(self):
        self.coords = None
        self.local_list = ['Главный квест', 'Побочный квест', 'Ловушка', 'Player']
        self.local = {}
        self.pos_loced = []
        for i in range(4):
            self.what_pos()
            while self.coords in self.pos_loced:
                self.what_pos()
            self.local[self.local_list[i]] = self.coords
            self.pos_loced.append(self.coords)

    def what_pos(self):
        pos = random.randint(0, 8)
        a = pos // 3
        b = pos % 3
        self.coords = (b, a)

    def get_self_local(self):
        return self.local

    def player_up_yl(self):
        pos_x = self.local['Player'][0]
        pos_y = self.local['Player'][1]
        self.local['Player'] = (pos_x, max(0, pos_y - 1))

    def player_down_yl(self):
        pos_x = self.local['Player'][0]
        pos_y = self.local['Player'][1]
        self.local['Player'] = (pos_x, min(2, pos_y + 1))

    def player_up_xl(self):
        pos_x = self.local['Player'][0]
        pos_y = self.local['Player'][1]
        self.local['Player'] = (min(pos_x + 1, 2), pos_y)

    def player_down_xl(self):
        pos_x = self.local['Player'][0]
        pos_y = self.local['Player'][1]
        self.local['Player'] = (max(pos_x - 1, 0), pos_y)

    def paint_icon(self, s):
        for i in self.local:
            if i == 'Главный квест' and self.local[i] != (-1, -1):
                s.blit(image.load('image/main_quest_icon.png'),
                       (714 + self.local[i][0] * 92, 15 + self.local[i][1] * 98))
            if i == 'Побочный квест' and self.local[i] != (-1, -1):
                s.blit(image.load('image/not_main_quest_icon.png'),
                       (714 + self.local[i][0] * 92, 15 + self.local[i][1] * 98))
            if i == 'Player' and self.local[i] != (-1, -1):
                s.blit(image.load('image/player_icon_local.png'),
                       (714 + self.local[i][0] * 92, 15 + self.local[i][1] * 98))

    def take_main(self):
        if self.local['Player'] == self.local['Главный квест']:
            return True
        else:
            return False

    def take_notmain(self):
        if self.local['Player'] == self.local['Побочный квест']:
            return True
        else:
            return False

    def take_lovuscha(self):
        if self.local['Player'] == self.local['Ловушка']:
            return True
        else:
            return False

    def del_ivent(self, ivent_name):
        self.local[ivent_name] = (-1, -1)
