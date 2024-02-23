from pygame import *
import random


def generate():
    local_list = ['Главный квест', 'Побочный квест', 'Ловушка', 'Player']
    local = {}
    pos_loced = []
    for i in range(4):
        pos = random.randint(0, 8)
        a = pos // 3
        b = pos % 3
        if i == 0:
            local[local_list[i]] = (b, a)
            pos_loced.append((b, a))
        else:
            while (b, a) in pos_loced:
                pos = random.randint(0, 8)
                a = pos // 3
                b = pos % 3
            local[local_list[i]] = (b, a)
            pos_loced.append((b, a))
    return local



class Forest_ivent:
    def __init__(self):
        self.description = '''Перед вами растирается огромный сумрачный лес, овеянный за века своего существования 
        множеством мифов и легенд. Главной из этих легенд по праву можно считать историю о волшебных грибах, растущих 
        на одной из центральных полянок. Если верить легендам, то эти грибы легко излечат раны, а также помогут 
        привлечь вдохновение, ну и за такие чудесные свойства их конечно можно дорого продать. 
        В этих лесах так же водятся ведьмы, к которым тоже не мешало бы заглянуть. Но в своих путешествиях стоит быть 
        осторожнее, ведь лес кишит волками и прочими опасностями.'''
        generate()

    















