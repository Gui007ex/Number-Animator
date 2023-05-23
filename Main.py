from Arqs.Canva import Canva
from Arqs.Animation import Animation
from os import system as sys

comands = '''1234 Animator - Versão 1.1


(G) criar animação
(A) selecionar animação
(C) configurações de animação


-----> '''
moves = '''(W) mover pra cima
(A) mover pra esquerda 
(S) mover pra baixo
(D) mover pra direita
(Número) trocar posição com esse número

-----> '''
configs = '''
(V) alterar velocidade
(N) alterar o nome
(X) excluir
(E) voltar

-----> '''

move_comands = ['W','S','D','A','1','2','3','4']
animations = []
debug_frame = 0

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
                            select -= 1
                    except:
                        pass
                animations[select].Play()
                input('\nEnter para voltar')
            else:
                input('\nSem animações :( ')
        case 'C':
            if len(animations):
                choosing = True
                while choosing:
                    sys('cls')
                    for i, animation in enumerate(animations):
                        print(f'{i+1} - {animation.Name()}')
                    try:
                        select = int(input("\nSelecionar animação para configurar: "))
                        if 0 < select <= len(animations):
                            choosing = False
                            select -= 1
                    except:
                        pass
                choosing = True
                while choosing:
                    sys('cls')
                    print(f'Selecionado: {animations[select].Name()}')
                    option = input(configs).upper()
                    match option:
                        case 'V':
                            sys('cls')
                            print(f'Velocidade atual: {1/animations[select].Speed()} fps\n')
                            new_speed = input('Selecione uma das velocidades:\n\n(1) fps\n(2) fps\n(4) fps\n(5) fps\n(8) fps\n(10) fps\n\n-----> ')
                            if new_speed in ['1','2','4','5','8','10']:
                                new_speed = int(new_speed)
                                animations[select].SetSpeed(1/new_speed)
                                input('\nVelocidade alterada ')
                        case 'N':
                            new_name = input('\nSelecione um novo nome: ')
                            animations[select].SetName(new_name)
                        case 'X':
                            password = animations[select].Name()
                            try_pass = input('\nConfirme o nome da animação para excluir: ')
                            if password == try_pass:
                                animations.pop(select)
                                input('\nAnimação excluída ')
                                choosing = False
                        case 'E':
                            choosing = False
            else:
                input('\nSem animações :( ')

