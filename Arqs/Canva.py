from os import system as sys

class Canva:
    def __init__(self) -> None:
        self.__matrix = [['-' for i in range(25)] for j in range(11)]
        self.__matrix[5] = ['-' for i in range(25)]
        self.__matrix[5][9], self.__matrix[5][11], self.__matrix[5][13], self.__matrix[5][15] = '1','2','3','4'
        self.__max_line = 11
        self.__max_row = 25
    
    def Show(self):
        for line in self.__matrix:
            print(''.join(line))

    def GetPosition(self, number):
        for i in range(len(self.__matrix)):
            if number in self.__matrix[i]:
                # Salvar a posição (y,x) do valor dentro da matriz
                line = i
                row = self.__matrix[i].index(number)
        return line, row
    
    def GetFrame(self):
        frame = [''.join(line).replace('-',' ') for line in self.__matrix]
        frame = '\n'.join(frame)
        return frame

    # Método de mover número selecionado para baixo no frame
    def __DownNumber(self, number):
        line, row = self.GetPosition(number) # Primeiro, procurar o número dentro da matriz
        self.__matrix[line][row] = '-'
        while  self.__matrix[(line+1)%self.__max_line][row] in '1234':
            line += 1
        self.__matrix[(line+1)%self.__max_line][row] = number # Usar a posição para alterar ela pra baixo

    # Método de mover número selecionado para cima no frame
    def __UpNumber(self, number):
        line, row = self.GetPosition(number)
        self.__matrix[line][row] = '-'
        while self.__matrix[line-1][row] in '1234':
            line -= 1
        self.__matrix[line-1][row] = number # Usar a posição para alterar ela pra cima

    # Método de mover número selecionado para a direita no frame
    def __RightNumber(self, number):
        line, row = self.GetPosition(number)
        self.__matrix[line][row] = '-'
        while self.__matrix[line][(row+1)%self.__max_row] in '1234':
            row += 1
        self.__matrix[line][(row+1)%self.__max_row] = number # Usar a posição para alterar ela pra direita

    # Método de mover número selecionado para a esquerda no frame 
    def __LeftNumber(self, number):
        line, row = self.GetPosition(number)
        self.__matrix[line][row] = '-'
        while self.__matrix[line][row-1] in '1234':
            row -= 1
        self.__matrix[line][row-1] = number # Usar a posição para alterar ela pra esquerda
    
    # Método para trocar a posição de 2 números
    def __SwapNumber(self, n1, n2):
        line_1, row_1 = self.GetPosition(n1)
        line_2, row_2 = self.GetPosition(n2)
        self.__matrix[line_1][row_1] = n2 
        self.__matrix[line_2][row_2] = n1 

    # Globalizador de movimento
    def Move(self, key, number):
        match key:
            case 'W':
                self.__UpNumber(number)
            case 'S':
                self.__DownNumber(number)
            case 'A':
                self.__LeftNumber(number)
            case 'D':
                self.__RightNumber(number)
            case '1' | '2' | '3' | '4':
                self.__SwapNumber(key, number)
