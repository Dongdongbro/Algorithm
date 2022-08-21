import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
result = 0
que = deque()
def bfs() :
    global result, que
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= M :
                continue
            if board[nx][ny] == 0 :
                board[nx][ny] = board[x][y] +1
                que.append((nx,ny))
                result = board[nx][ny]
            if board[nx][ny] == -1 :
                continue
    for i in range(N):
        for j in range(M) :
            if board[i][j] == 0 :
                return -1
    if result == 0 :
        return result
    else :
        return result -1

for i in range(N) :
    for j in range(M) :
        if board[i][j]==1 :
            que.append((i,j))
print(bfs())
