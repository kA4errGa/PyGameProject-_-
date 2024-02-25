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
        self.par_name_font = font.Font('Merriweather/Merriweather-Regular.ttf', 19)
        self.text_par_name = (self.par_name_font).render('Характеристики', True, (255, 255, 255))
        s.blit(self.text_par_name, (14, 20))
        self.par_life_font = font.Font('Merriweather/Merriweather-Regular.ttf', 25)
        self.text_life_name = (self.par_life_font).render(f'Жизнь: {self.param_life}/{self.param_life_max}', True,
                                                          'red')
        s.blit(self.text_life_name, (14, 60))
        self.par_power_font = font.Font('Merriweather/Merriweather-Regular.ttf', 20)
        self.text_power_name = (self.par_power_font).render(f'Энергия: {self.param_power}/{self.param_power_max}', True,
                                                            'blue')
        s.blit(self.text_power_name, (14, 160))
        self.par_mony_font = font.Font('Merriweather/Merriweather-Regular.ttf', 24)
        self.text_mony_name = (self.par_mony_font).render(f'Деньги: {self.param_mony}/{self.param_mony_max}', True,
                                                          'yellow')
        s.blit(self.text_mony_name, (14, 260))

    def par_up(self, name, a):
        if name == 'life':
            self.new_par_life = self.param_life + a
            self.param_life = max(0, self.new_par_life)
            self.new_par_life = self.param_life
            self.param_life = min(self.param_life_max, self.new_par_life)
        if name == 'max_life':
            self.param_life_max = max(0, self.param_life_max + a)
            if self.param_life_max < self.param_life:
                self.param_life = self.param_life_max
        if name == 'power':
            self.new_par_power = self.param_power + a
            self.param_power = max(0, self.new_par_power)
            self.new_par_power = self.param_power
            self.param_power = min(self.param_power_max, self.new_par_power)
        if name == 'max_power':
            self.param_power_max = max(0, self.param_power_max + a)
            if self.param_power_max < self.param_power:
                self.param_power = self.param_power_max
        if name == 'mony':
            self.new_par_mony = self.param_mony + a
            self.param_mony = max(0, self.new_par_mony)
            self.new_par_mony = self.param_mony
            self.param_mony = min(self.param_mony_max, self.new_par_mony)
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
