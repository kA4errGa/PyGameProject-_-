from pygame import *
# Файл в котором содержатся классы всех локаций


# Класс Локации 'Сумрачный лес'
class Forest_ivent:
    def __init__(self):
        self.description = ['Перед вами простирается огромный сумрачный лес,',
                            'овеянный за века своего существования множеством',
                            'мифов и легенд. Главной из этих легенд по праву можно',
                            'считать историю о волшебных грибах, растущих на одной',
                            'из центральных полянок. Если верить легендам, то эти',
                            'грибы легко излечат раны, а также помогут привлечь',
                            'вдохновение, ну и за такие чудесные свойства их конечно',
                            'можно дорого продать. В этих лесах так же водятся ведьмы,',
                            'к которым тоже не мешало бы заглянуть.',
                            'Но в своих путешествиях стоит быть осторожнее,',
                            'ведь лес кишит волками и прочими опасностями.']
        self.m_quest = ['Вам удалось добраться до заветной полянки. Вроде бы…',
                        'Ну может вон за тем деревом? Тоже нет. Вы понимаете,',
                        'что походу заблудились и продолжать поиски бессмысленно,',
                        'и тут же находите тропинку, которая сможет вывести вас',
                        'из леса.',
                        'Как же вы поступите: Продолжите искать волшебные грибы,',
                        'или же сдадитесь и выйдете из леса']
        self.nm_quest = ['Кажется, вам удалось найти логово ведьм. ',
                         'Непонятно как вы это поняли. ',
                         'То ли по котлу и развешенным вокруг него травам, ',
                         'толи по трём уродливым старухам, кружащим около ',
                         'этого котла.Увидев их, вы передумали с ними знакомиться, ',
                         'однако они походу завидев вас напротив захотели ',
                         'пообщаться с вами. Тебе чё тут надо? Спрашивает',
                         'одна из них. ',
                         'Как вы ответите?']
        self.l_quest = ['Идёте вы себе спокойно по лесу как вдруг вылетают дикие ',
                        'волки. Неприятно, но нужно что-то срочно придумывать. ',
                        'Можно попытаться сбежать, потратив кучу сил или ',
                        'попытаться отбиться, потратив здоровье.',
                        'Что вы предпримете?']
        self.descfont = font.Font('Merriweather/Merriweather-Regular.ttf', 15)

    # метод вывода описания локации при входе в неё
    def out_dis(self, s):
        for i in range(len(self.description)):
            self.desc_text = (self.descfont).render(self.description[i], True, 'green')
            s.blit(self.desc_text, (204, 14 + i * 17))

    # методы выводящие развитие событий при прохождении событий локации
    def mainquest(self, s):
        for i in range(len(self.m_quest)):
            self.main_text = (self.descfont).render(self.m_quest[i], True, 'green')
            s.blit(self.main_text, (204, 14 + i * 17))
        self.text_btn_l1 = (self.descfont).render('ПРОДОЛЖИТЬ ИСКАТЬ', True, 'green')
        s.blit(self.text_btn_l1, (214, 515))
        self.text_btn_l2 = (self.descfont).render('УЙТИ', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))

    def notmainquest(self, s):
        for i in range(len(self.nm_quest)):
            self.notmain_text = (self.descfont).render(self.nm_quest[i], True, 'green')
            s.blit(self.notmain_text, (204, 14 + i * 17))
        self.text_btn_l1 = (self.descfont).render('ВАС ПОВИДАТЬ', True, 'green')
        s.blit(self.text_btn_l1, (214, 473))
        self.text_btn_l1 = (self.descfont).render('ДЕНЕГ', True, 'green')
        s.blit(self.text_btn_l1, (214, 515))
        self.text_btn_l2 = (self.descfont).render('СЛАВЫ', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))

    def lovuschaquest(self, s):
        for i in range(len(self.l_quest)):
            self.lovuscha_text = (self.descfont).render(self.l_quest[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
        self.text_btn_l1 = (self.descfont).render('ПОПЫТАТЬСЯ БЕЖАТЬ', True, 'green')
        s.blit(self.text_btn_l1, (214, 515))
        self.text_btn_l2 = (self.descfont).render('ПОПЫТАТЬСЯ ОТБИТЬСЯ', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))

    def vibor_l(self, s):
        self.text_btn_l1 = (self.descfont).render('Вам удалось спастись', True, 'green')
        self.text_btn_l2 = (self.descfont).render('ХОРОШО', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))
        s.blit(self.text_btn_l1, (204, 14))

    def vibor_nm_p(self, s):
        self.nm_op = ['Услышав ваш ответ ведьмы ухмыляются.', 'А чего отдал бы: здоровья или сил?']
        for i in range(len(self.nm_op)):
            self.lovuscha_text = (self.descfont).render(self.nm_op[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
        self.text_btn_l1 = (self.descfont).render('ЗДОРОВЬЯ', True, 'green')
        s.blit(self.text_btn_l1, (214, 515))
        self.text_btn_l1 = (self.descfont).render('СИЛ', True, 'green')
        s.blit(self.text_btn_l1, (214, 557))

    def vibor_nm(self, s):
        self.nm_op = ['Правильно мыслишь, ну вот тебе чего хотел. Сказав это, ',
                      'ведьма махнула рукой и, вы заснули. Спустя время ',
                      'вы пришли себя на какой-то полянке с головной болью, ',
                      'но зато c тем что искали. ',
                      '«Ну хоть жив остался» - резюмировали вы.']
        for i in range(len(self.nm_op)):
            self.lovuscha_text = (self.descfont).render(self.nm_op[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
        self.text_btn_l2 = (self.descfont).render('ХОРОШО', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))

    def vibor_nmb(self, s):
        self.nm_op = ['Ну раз жадный такой придётся тебе урок преподать, чтоб не жадничал! ',
                      'Не будет у тебя больше ни сил, ни здоровья! Сказав это, ведьма махнула рукой и, ',
                      'вы заснули. Спустя время вы пришли себя на какой-то полянке обессиленными, без денег и славы.']
        for i in range(len(self.nm_op)):
            self.lovuscha_text = (self.descfont).render(self.nm_op[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
        self.text_btn_l2 = (self.descfont).render('ОЙ', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))

    def vibor_fast_skeep(self, s):
        self.nm_op = ['Увидел? Ну и чеши отсюда пока при памяти. ',
                      'Бесцеремонно говорит одна из них. ',
                      'Вы не то чтобы были против такого развития ',
                      'ситуации уходите ни с чем.']
        for i in range(len(self.nm_op)):
            self.lovuscha_text = (self.descfont).render(self.nm_op[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
            self.text_btn_l2 = (self.descfont).render('НУ ХОТЬ ЖИВ ОСТАЛСЯ', True, 'green')
            s.blit(self.text_btn_l2, (214, 557))

    def mainquest_p(self, s):
        self.nm_op = ['Побродив ещё битый час по лесу вам всё-таки ',
                      'удаётся найти заветные грибы. Их фиолетовое мерцание ',
                      'манит вас. Как вы ими распорядитесь?']
        for i in range(len(self.nm_op)):
            self.lovuscha_text = (self.descfont).render(self.nm_op[i], True, 'green')
            s.blit(self.lovuscha_text, (204, 14 + i * 17))
        self.text_btn_l2 = (self.descfont).render('СДЕЛАТЬ ЛЕКАРСТВО', True, 'green')
        s.blit(self.text_btn_l2, (214, 557))
        self.text_btn_l2 = (self.descfont).render('СДЕЛАТЬ ЭЛИКСИР ВДОХНОВЕНИЯ', True, 'green')
        s.blit(self.text_btn_l2, (214, 515))
        self.text_btn_l2 = (self.descfont).render('ПРОДАТЬ НА МЕСТНОМ РЫНКЕ', True, 'green')
        s.blit(self.text_btn_l2, (214, 473))
