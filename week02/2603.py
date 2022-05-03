import sys

n = int(sys.stdin.readline())
board = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]


def partition (x,y,num) :
    global count_blue, count_white
    color = board[x][y]
    for i in range(x,x+num) :
        for j in range(y,y+num) :
            if color != board[i][j] :
                #1사분면
                partition(x,y,num//2)
                #2사분면
                partition(x,y+num//2,num//2)
                #3사분면
                partition(x+num//2,y,num//2)
                #4사분면
                partition(x+num//2,y+num//2,num//2)
                return
    if color == 1 :
        count_blue += 1
        return
    else :
        count_white += 1
        return
count_blue, count_white = 0, 0
partition(0,0,n)
print(count_white)
print(count_blue)
