from pygame import *


class Parametrs:
    def __init__(self):
        self.param_life = 5
        self.param_life_max = 10
        self.param_power = 5
        self.param_power_max = 10
        self.param_mony = 5
        self.param_mony_max = 10

    def paint_par(self, s):
        par_name_font = font.Font('Merriweather/Merriweather-Regular.ttf', 19)
        text_par_name = par_name_font.render('Характеристики', True, (255, 255, 255))
        s.blit(text_par_name, (14, 20))
        par_life_font = font.Font('Merriweather/Merriweather-Regular.ttf', 25)
        self.text_life_name = par_life_font.render(f'Жизнь: {self.param_life}/{self.param_life_max}', True,
                                                          'red')
        s.blit(self.text_life_name, (14, 60))
        par_power_font = font.Font('Merriweather/Merriweather-Regular.ttf', 20)
        text_power_name = par_power_font.render(f'Энергия: {self.param_power}/{self.param_power_max}', True,
                                                            'blue')
        s.blit(text_power_name, (14, 160))
        par_mony_font = font.Font('Merriweather/Merriweather-Regular.ttf', 24)
        text_mony_name = (par_mony_font).render(f'Деньги: {self.param_mony}/{self.param_mony_max}', True,
                                                          'yellow')
        s.blit(text_mony_name, (14, 260))

    def par_up(self, name, a):
        if name == 'life':
            new_par_life = self.param_life + a
            param_life = max(0, new_par_life)
            new_par_life = param_life
            self.param_life = min(self.param_life_max, new_par_life)
        if name == 'max_life':
            self.param_life_max = max(0, self.param_life_max + a)
            if self.param_life_max < self.param_life:
                self.param_life = self.param_life_max
        if name == 'power':
            new_par_power = self.param_power + a
            param_power = max(0, new_par_power)
            new_par_power = param_power
            self.param_power = min(self.param_power_max, new_par_power)
        if name == 'max_power':
            self.param_power_max = max(0, self.param_power_max + a)
            if self.param_power_max < self.param_power:
                self.param_power = self.param_power_max
        if name == 'mony':
            new_par_mony = self.param_mony + a
            param_mony = max(0, new_par_mony)
            new_par_mony = param_mony
            self.param_mony = min(self.param_mony_max, new_par_mony)
        if name == 'max_mony':
            self.param_mony_max = max(0, self.param_mony_max + a)
            if self.param_mony_max < self.param_mony:
                self.param_mony = self.param_mony_max

    def life_not_zero(self):
        if self.param_life > 0:
            return True
        else:
            return False

    def power_not_zero(self):
        if self.param_power > 0:
            return True
        else:
            return False
