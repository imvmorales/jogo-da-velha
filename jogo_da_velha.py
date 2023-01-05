aux = ' '
token = ['X', 'O']

def criaBoard():
    board = [
        [aux, aux, aux],
        [aux, aux, aux],
        [aux, aux, aux],
    ]
    return board


def printBoard(board):
    for i in range(3):
        print('|'.join(board[i]))
        if i < 2:
            print('------')


def getInput(msg):
    try:
        n = int(input(msg))
        if n >= 1 and n <= 3:
            return n - 1
        else:
            print('Por favor, digite um número entre 1 e 3')
            return getInput(msg)
    except:
        print('Número inválido')
        return getInput(msg)


def verificaMovimento(board, linha, coluna):
    if board[linha][coluna] == aux:
        return True
    else:
        return False


def movimento(board, linha, coluna, jogador):
    board[linha][coluna] = token[jogador]


def verificaGanhador(board):
    # linhas
    for i in range(3):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2] and board[i][0] != aux:
            return board[i][0]

    # colunas
    for i in range(3):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != aux:
            return board[0][i]

    # diagonal principal
    if board[0][0] != aux and board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        return board[0][0]

    # diagonal secundária
    if board[0][2] != aux and board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]

    for i in range(3):
        for j in range(3):
            if board[i][j] == aux:
                return False

    return 'EMPATE'
