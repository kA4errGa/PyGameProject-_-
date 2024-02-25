from pygame import *
from GlobalPole import GlobalPole
from LegendPole import LegendPole
from Score import Score
from Parametrs import Parametrs
from LocalPole import LocalPole
from Ivets import Forest_ivent

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

forest = Forest_ivent()
Player_position = 'Global'
main_p = GlobalPole()
local_p = LocalPole()
legend = LegendPole(main_p.get_self_local())
score = Score(0)
parametrs = Parametrs()
block = Surface((492, 572))
block.fill((0, 0, 0))

Player_ivent = None
choice = None
vibor = False
skeep_l = False
skeep_nm = False
ansv_nm = False
trig = None
ansv_nm_b = False

running = True

while running:

    screen.blit(image.load('image/1620268386_21-phonoteka_org-p-fon-iz-mobilnikh-igr-22.jpg'), (0, 0))
    PaintRamochca(180, 380, 10, 10)
    PaintRamochca(180, 190, 10, 400)
    PaintLocalPole()
    PaintRamochca(280, 200, 710, 390)
    legend.paint_legend(screen)
    score.paint_score(screen)
    parametrs.paint_par(screen)
    if Player_position == 'Global':
        PaintMainPole()
        main_p.paint_icon(screen)
    if Player_position == 'Local' or Player_position == 'Local_S':
        main_p.paint_icon(screen)
        PaintRamochca(500, 580, 200, 10)
        local_p.paint_icon(screen)

        if Player_ivent == 'Сумрачный лес':
            main_p.del_ivent('Сумрачный лес')
            forest.out_dis(screen)
            if local_p.take_main():
                Player_position = 'Local_S'
                PaintRamochca(500, 580, 200, 10)
                PaintRamochca(480, 28, 210, 552)
                PaintRamochca(480, 28, 210, 510)
                forest.mainquest(screen)
                if choice == 0 and not (vibor):
                    parametrs.par_up('power', -1)
                    choice = None
                    Player_position = 'Global'
                if choice == 1 and not (vibor):
                    parametrs.par_up('power', -3)
                    choice = None
                    vibor = True
                if vibor:
                    PaintRamochca(500, 580, 200, 10)
                    PaintRamochca(480, 28, 210, 552)
                    PaintRamochca(480, 28, 210, 510)
                    PaintRamochca(480, 28, 210, 468)
                    forest.mainquest_p(screen)
                    ansv_nm = False
                    if choice == 0:
                        parametrs.par_up('life', 3)
                        score.score_up(100)
                        choice = None
                        vibor = False
                        Player_position = 'Global'
                    if choice == 1:
                        score.score_up(500)
                        choice = None
                        vibor = False
                        Player_position = 'Global'
                    if choice == 2:
                        parametrs.par_up('mony', 3)
                        score.score_up(100)
                        choice = None
                        vibor = False
                        Player_position = 'Global'
            if local_p.take_notmain():
                Player_position = 'Local_S'
                PaintRamochca(500, 580, 200, 10)
                PaintRamochca(480, 28, 210, 552)
                PaintRamochca(480, 28, 210, 510)
                PaintRamochca(480, 28, 210, 468)
                forest.notmainquest(screen)
                if choice == 0 and not (vibor):
                    trig = 0
                    choice = None
                    vibor = True
                if choice == 1 and not (vibor):
                    trig = 1
                    choice = None
                    vibor = True
                if choice == 2 and not (vibor):
                    trig = 2
                    choice = None
                    vibor = True
                if vibor and trig != 2:
                    PaintRamochca(500, 580, 200, 10)
                    PaintRamochca(480, 28, 210, 552)
                    PaintRamochca(480, 28, 210, 510)
                    forest.vibor_nm_p(screen)
                    if choice == 0:
                        parametrs.par_up('power', -1)
                        choice = None
                        if trig == 1:
                            parametrs.par_up('mony', 1)
                            trig = None
                        if trig == 0:
                            score.score_up(50)
                            trig = None
                        ansv_nm = True
                    if choice == 1:
                        parametrs.par_up('life', -1)
                        choice = None
                        if trig == 1:
                            parametrs.par_up('mony', 1)
                            trig = None
                        if trig == 0:
                            score.score_up(50)
                            trig = None
                        ansv_nm = True
                        choice = None
                    if ansv_nm:
                        PaintRamochca(500, 580, 200, 10)
                        PaintRamochca(480, 28, 210, 552)
                        forest.vibor_nm(screen)

                    if skeep_nm:
                        local_p.del_ivent('Побочный квест')
                        Player_position = 'Local'
                        vibor = False
                        choice = None
                if vibor and trig == 2:
                    PaintRamochca(500, 580, 200, 10)
                    PaintRamochca(480, 28, 210, 552)
                    forest.vibor_fast_skeep(screen)
                    ansv_nm = True
                    choice = None
                    if ansv_nm:
                        PaintRamochca(500, 580, 200, 10)
                        PaintRamochca(480, 28, 210, 552)
                        forest.vibor_fast_skeep(screen)

                    if skeep_nm:
                        local_p.del_ivent('Побочный квест')
                        Player_position = 'Local'
                        vibor = False
                        choice = None
                        ansv_nm = False
            if local_p.take_lovuscha():
                Player_position = 'Local_S'
                PaintRamochca(500, 580, 200, 10)
                PaintRamochca(480, 28, 210, 552)
                PaintRamochca(480, 28, 210, 510)
                forest.lovuschaquest(screen)
                if choice == 0:
                    parametrs.par_up('life', -2)
                    choice = None
                    vibor = True
                if choice == 1:
                    parametrs.par_up('power', -1)
                    choice = None
                    vibor = True
                if vibor:
                    PaintRamochca(500, 580, 200, 10)
                    PaintRamochca(480, 28, 210, 552)
                    forest.vibor_l(screen)
                    if skeep_l:
                        local_p.del_ivent('Ловушка')
                        Player_position = 'Local'
                        vibor = False

    if main_p.player_take_ivent():
        Player_position = 'Local'
        Player_ivent = main_p.player_take_ivent()
    for ev in event.get():
        if ev.type == QUIT:
            quit()
            running = False
        if Player_position == 'Local':
            if ev.type == KEYDOWN:
                if ev.key == K_w:
                    local_p.player_up_yl()
                if ev.key == K_s:
                    local_p.player_down_yl()
                if ev.key == K_d:
                    local_p.player_up_xl()
                if ev.key == K_a:
                    local_p.player_down_xl()
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
        if Player_position == 'Local_S' and not (vibor):
            if ev.type == MOUSEBUTTONDOWN:
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 472 and ev.pos[1] <= 492):
                    choice = 2
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 514 and ev.pos[1] <= 534):
                    choice = 1
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 556 and ev.pos[1] <= 576):
                    choice = 0
        if (Player_position == 'Local_S' and vibor and local_p.take_lovuscha()) or (Player_position == 'Local_S' and local_p.take_notmain() and ansv_nm):
            if ev.type == MOUSEBUTTONDOWN:
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 556 and ev.pos[1] <= 576) and local_p.take_lovuscha():
                    skeep_l = True
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 556 and ev.pos[1] <= 576) and local_p.take_notmain():
                    skeep_nm = True
        if Player_position == 'Local_S' and vibor and (local_p.take_notmain() or local_p.take_main()) and not(ansv_nm):
            if ev.type == MOUSEBUTTONDOWN:
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 472 and ev.pos[1] <= 492):
                    choice = 2
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 514 and ev.pos[1] <= 534):
                    choice = 1
                if (ev.pos[0] >= 214 and ev.pos[0] <= 686) and (ev.pos[1] >= 556 and ev.pos[1] <= 576):
                    choice = 0

    if not (parametrs.life_not_zero() and parametrs.power_not_zero()):
        running = False
    display.flip()
