import tests
import time
import game
from os import system

size=int(input("Insert size of board: "))
board=[[' ',' ','x',' ',' ',' ',' '],
       ['x',' ','x',' ',' ',' ',' '],
       [' ','x','x',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' '],
       [' ',' ',' ',' ',' ',' ',' ']]

while True:
    system("clear")
    tests.printBoard(board,size)
    board=game.nextRound(board,size)
    time.sleep(1)

