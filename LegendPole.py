from pygame import *


class LegendPole:
    def __init__(self, data):
        self.names = [i for i in data]
        self.count = 0

    def paint_legend(self, s):
        for i in range(4):
            y_cord = 390 + 49 * i
            if self.names[i] == 'Сумрачный лес':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                text = mainfont.render('Сумрачный лес', True, 'green')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Сокровищница дракона':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 20)
                text = mainfont.render('Сокровищница дракона', True, 'red')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Большой город':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                text = mainfont.render('Большой город', True, 'blue')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Логово чародея':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                text = mainfont.render('Логово чародея', True, 'purple')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Деревня':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                text = mainfont.render('Деревня', True, 'orange')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Хлебные поля':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 30)
                text = mainfont.render('Хлебные поля', True, 'yellow')
                s.blit(text, (714, y_cord))
            if self.names[i] == 'Эльфийское озеро':
                mainfont = font.Font('Merriweather/Merriweather-Regular.ttf', 26)
                text = mainfont.render('Эльфийское озеро', True, 'cyan')
                s.blit(text, (714, y_cord))
            self.count += 1
