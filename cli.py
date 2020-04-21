from os import system
import time
import game
import tests
import ast

def printBoardNum(board,size):
    for i in range(size):
        for j in range(size+1):
            if j==size:
                print("{}".format(i))
            else:
                print(board[i][j],end='|')

    for i in range(size):
        print(i,end=" ")

size=int(input("Please enter size of the board (you only have to type on number since its square): "))
board = [[' ' for x in range(size)] for y in range(size)]

while True:
    system("clear")
    printBoardNum(board,size)
    a=ast.literal_eval(input("Please enter in what row and column you would like to place a living cell (examplle input \"1,2\"), if you are done type \"-1\":  "))
    if a==-1: break

    if board[a[0]][a[1]]=='x':
        board[a[0]][a[1]]=' '
    else:
        board[a[0]][a[1]]='x'
    
while True:
    system("clear")
    tests.printBoard(board,size)
    board=game.nextRound(board,size)
    time.sleep(1)