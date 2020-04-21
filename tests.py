import game

def printNeigh(board,size):
    for i in range(size):
        for j in range(size):
            print(game.neighbours(board,size,i,j),end=',')
        print()

def printBoard(board,size):
    for i in range(size):
        for j in range(size):
            print(board[i][j],end='|')
        print()
