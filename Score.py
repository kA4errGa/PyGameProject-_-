from pygame import *


class Score:
    def __init__(self, data):
        self.max_score = data
        self.score = 0

    def paint_score(self, s):
        self.scorenamefont = font.Font('Merriweather/Merriweather-Regular.ttf', 50)
        self.textscorename = (self.scorenamefont).render('Счёт', True, (255, 255, 255))
        s.blit(self.textscorename, (34, 404))
        self.scorefont = font.Font('Merriweather/Merriweather-Regular.ttf', 50)
        self.textscore = (self.scorefont).render(str(self.score), True, (255, 255, 255))
        s.blit(self.textscore, (34, 504))

    def score_up(self, a):
        self.score += a
