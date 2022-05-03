import sys
input = sys.stdin.readline

a = int(input())
board = [list(map(int,input().split())) for i in range(a)]
count_w, count_b = 0, 0

def color_search (x,y,num) :
    global count_w, count_b
    color = board[x][y]
    for i in range(x, x+num) :
        for j in range(y, y+num) :
            if color != board[i][j] :
                #1사분면
                color_search(x,y,num//2)
                #2사분면
                color_search(x,y+num//2,num//2)
                #3사분면
                color_search(x+num//2,y,num//2)
                #4사분면
                color_search(x+num//2,y+num//2,num//2)
                return
    if color == 1 :
        count_b +=1
        return
    else :
        count_w +=1
        return

color_search(0,0,a)
print(count_b)
print(count_w)