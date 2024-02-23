from pygame import *
from GlobalPole import GlobalPole
from LegendPole import LegendPole
from Score import Score
from Parametrs import Parametrs

init()


def PaintMainPole():
    PaintMainPole_square_main = Surface((500, 580))
    PaintMainPole_square_main.fill((255, 255, 255))
    screen.blit(PaintMainPole_square_main, (200, 10))
    PaintMainPole_square_main_clet = Surface((58, 68))
    PaintMainPole_square_main_clet.fill((0, 0, 0))
    for x in range(204, 639, 62):
        for y in range(14, 527, 72):
            screen.blit(PaintMainPole_square_main_clet, (x, y))


def PaintLocalPole():
    PaintLocalPole_square_main = Surface((280, 300))
    PaintLocalPole_square_main.fill((255, 255, 255))
    screen.blit(PaintLocalPole_square_main, (710, 10))
    PaintLocalPole_square_main_clet = Surface((88, 94))
    PaintLocalPole_square_main_clet.fill((0, 0, 0))
    for x in range(714, 899, 92):
        for y in range(15, 220, 98):
            screen.blit(PaintLocalPole_square_main_clet, (x, y))


def PaintRamochca(Paint_s, Paint_h, Paint_x, Paint_y):
    PaintRecPole_square_poias = Surface((Paint_s, Paint_h))
    PaintRecPole_square_poias.fill((255, 255, 255))
    screen.blit(PaintRecPole_square_poias, (Paint_x, Paint_y))
    PaintRecPole_square_poias1 = Surface((Paint_s - 8, Paint_h - 8))
    PaintRecPole_square_poias1.fill((0, 0, 0))
    screen.blit(PaintRecPole_square_poias1, (Paint_x + 4, Paint_y + 4))


size = (1000, 600)
screen = display.set_mode(size)
display.set_caption("ЛУЧШАЯ В МИРЕ ИГРА")
display.set_icon(image.load('image/icon_prilojenia.jpg'))

Player_position = 'Global'
main_p = GlobalPole()
legend = LegendPole(main_p.get_self_local())
score = Score(0)
parametrs = Parametrs()

running = True

while running:

    screen.blit(image.load('image/1620268386_21-phonoteka_org-p-fon-iz-mobilnikh-igr-22.jpg'), (0, 0))
    PaintMainPole()
    PaintRamochca(180, 380, 10, 10)
    PaintRamochca(180, 190, 10, 400)
    PaintLocalPole()
    PaintRamochca(280, 200, 710, 390)
    main_p.paint_icon(screen)
    legend.paint_legend(screen)
    score.paint_score(screen)
    parametrs.paint_par(screen)

    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
        if Player_position == 'Global':
            if ev.type == KEYDOWN:
                if ev.key == K_w:
                    main_p.player_up_y()
                if ev.key == K_s:
                    main_p.player_down_y()
                if ev.key == K_d:
                    main_p.player_up_x()
                if ev.key == K_a:
                    main_p.player_down_x()
            if main_p.player_take_ivent():
                Player_position = 'Local'
 #   while Player_position == 'Local':

           #     if main_p.player_take_ivent() == 'Сумрачный лес':
#
           #     if main_p.player_take_ivent() == 'Сокровищница дракона':
           #     if main_p.player_take_ivent() == 'Большой город':
           #     if main_p.player_take_ivent() == 'Логово чародея':
           #     if main_p.player_take_ivent() == 'Деревня':
           #     if main_p.player_take_ivent() == 'Хлебные поля':
           #     if main_p.player_take_ivent() == 'Эльфийское озеро':

    display.flip()
