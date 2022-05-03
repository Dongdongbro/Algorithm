import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
T = int(input())



def dfs(x,y) :
    if x<0 or y<0 or x>=N or y>=M :
        return False
    if board[x][y] == 1 :
        board[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False



for i in range(T) :
    result =0
    M,N,K= map(int,input().split())
    board = [[0 for i in range(M)] for j in range(N)]
    for j in range(K) :
        a, b = map(int,input().split())
        board[b][a] =1

    for i in range(N):
        for j in range(M) :
            if dfs(i,j) == True :
                result +=1
    print(result,end='\n')
