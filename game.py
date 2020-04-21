def neighbours(board,size,x,y):

    if(board[x][y]=='x'):
        sm=-1
    else:
        sm=0

    x-=1 
    y-=1

    for i in range(3):
        for j in range(3):
            if(board[map(x+i,size)][map(y+j,size)]=='x'):
                sm+=1
            
    return sm

def nextState(a,neigh):
    if a==' ':
        if neigh==3:
            return 'x'
        else:
            return ' '
    if a=='x':
        if neigh in [2,3]:
            return 'x'
        else:
            return ' '

def nextRound(board,size):

    new = [['0' for x in range(size)] for y in range(size)] 
    for i in range(size):
        for j in range(size):
            neigh=neighbours(board,size,i,j)
            new[i][j]=nextState(board[i][j],neigh)

    return new

def map(a,size):
    if(a==-1): return size-1
    if(a==size): return 0
    return a

