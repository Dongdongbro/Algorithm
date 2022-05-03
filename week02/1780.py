import sys
input = sys.stdin.readline
a = int(input())

board = [list(map(int,input().split())) for i in range(a)]
zero_cnt = 0
one_cnt = 0
minus_cnt = 0

def num_search(x,y,num) :
    global zero_cnt, one_cnt, minus_cnt
    chk = board[x][y]

    for i in range(x, x+num) :
        for j in range(y, y+num) :
            if chk != board[i][j] :
                num_search(x,y,num//3)#1사분면
                num_search(x,y+num//3,num//3) #2사분면
                num_search(x,y+2*num//3,num//3) #3사분면
                num_search(x+num//3,y,num//3)#4사분면
                num_search(x+num/3,y+num//3,num//3) #5사분면
                num_search(x+num//3,y+2*num//3,num//3)#6사분면
                num_search(x+2*num//3,y,num//3) #7사분면
                num_search(x+2*num//3,y+num//3,num//3) #8사분면
                num_search(x+2*num//3,y+2*num//3,num//3) # 9사분면
                return
    if chk == 0 :
        zero_cnt += 1
        return
    elif chk == 1 :
        one_cnt += 1
        return
    else :
        minus_cnt += 1
        return

num_search(0,0,a)
print(minus_cnt)
print(zero_cnt)
print(one_cnt)


