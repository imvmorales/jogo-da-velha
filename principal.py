from jogo_da_velha import criaBoard, printBoard, getInput, verificaMovimento,\
    movimento, verificaGanhador

jogador = 0
board = criaBoard()
ganhador = verificaGanhador(board)

while not ganhador:
    printBoard(board)
    linha = getInput('Digite a linha: ')
    coluna = getInput('Digite a coluna: ')

    if verificaMovimento(board, linha, coluna):
        movimento(board, linha, coluna, jogador)
        jogador = (jogador + 1) % 2
    else:
        print('A posição informada já está ocupada, tente novamente')

    ganhador = verificaGanhador(board)

print('==================')
printBoard(board)
print('Ganhador = ', ganhador)
print('==================')
