from Arqs.Canva import Canva
from Arqs.Animation import Animation
from os import system as sys

tutorial = open(file='Arqs/Tutorial.txt',mode='r',encoding='utf-8').read()
comands = open(file='Arqs/Comands.txt',mode='r',encoding='utf-8').read()
moves = open(file='Arqs/Move_Options.txt',mode='r',encoding='utf-8').read()

move_comands = ['W','S','D','A','1','2','3','4']
animations = []
debug_frame = 0

# sys('cls')
# input(tutorial)

while True: 
    sys('cls')
    entry = input(comands).upper()

    match entry:
        case 'G':
            preview = Canva()
            building, frame, end_warn = True, 1, ''
            frames = []
            while building:
                sys('cls')
                print(f'Editor - Frame {frame}\n(P) para salvar frame{end_warn}\n')
                preview.Show()
                number = input('\nSelecione o número: ').upper()
                if number in ['1','2','3','4']:
                    moving_number = True
                    while moving_number:
                        sys('cls')
                        print(f'Editor - Frame {frame}\n(P) para salvar frame{end_warn}\n')
                        preview.Show()
                        print(f'\nSelecionado: {number}\n')
                        key = input(moves).upper()
                        if key == '':
                            moving_number = False
                        elif key in move_comands:
                            preview.Move(key, number)
                elif number == 'P':
                    frames.append(preview.GetFrame())
                    frame += 1
                elif number == 'F' and frame > 2:
                    building = False
                    anim_name = input('\nNome da animação: ')
                    new_animation = Animation(frames, anim_name)
                    animations.append(new_animation)
                if frame > 2:
                    end_warn = '\n(F) para finalizar'
        case 'A':
            if len(animations):
                choosing = True
                while choosing:
                    sys('cls')
                    for i, animation in enumerate(animations):
                        print(f'{i+1} - {animation.Name()}')
                    try:
                        select = int(input("\nSelecionar animação para rodar: "))
                        if 0 < select <= len(animations):
                            choosing = False
                    except:
                        pass
                animations[select-1].Play()
                input('\nEnter para voltar')
            else:
                input('\nSem animações :( ')