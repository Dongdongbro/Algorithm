import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().split())
board = []
virus = []
for i in range(N) :
    board.append(list(map(int,input().split())))
    for j in range(N) :
        if board[i][j]!=0 :
            virus.append((board[i][j],i,j))
S,X,Y = map(int, input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
que = deque(virus)

result =0
while que:
    if result == S :
        break
    for _ in range(len(que)):
        p, x, y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if board[nx][ny] == 0 :
                    board[nx][ny] = board[x][y]
                    que.append((board[nx][ny],nx,ny))
    result += 1
virus.sort()
print(board[X-1][Y-1])