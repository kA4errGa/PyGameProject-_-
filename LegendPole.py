from pygame import *


class LegendPole:
    def __init__(self, data):
        self.names = [i for i in data]
        self.count = 0

    def paint_legend(self, s):
        for i in range(4):
            self.y_cord = 390 + 49 * i
            if self.names[i] == 'Сумрачный лес':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                self.text = (self.mainfont).render('Сумрачный лес', True, 'green')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Сокровищница дракона':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 20)
                self.text = (self.mainfont).render('Сокровищница дракона', True, 'red')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Большой город':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                self.text = (self.mainfont).render('Большой город', True, 'blue')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Логово чародея':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                self.text = (self.mainfont).render('Логово чародея', True, 'purple')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Деревня':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                self.text = (self.mainfont).render('Деревня', True, 'orange')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Хлебные поля':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                self.text = (self.mainfont).render('Хлебные поля', True, 'yellow')
                s.blit(self.text, (714, self.y_cord))
            if self.names[i] == 'Эльфийское озеро':
                self.mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 26)
                self.text = (self.mainfont).render('Эльфийское озеро', True, 'cyan')
                s.blit(self.text, (714, self.y_cord))
            self.count += 1
