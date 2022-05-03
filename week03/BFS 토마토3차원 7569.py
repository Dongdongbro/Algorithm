import sys
from collections import deque
input = sys.stdin.readline
M, N, H = map(int, input().split())
board = []
for i in range(N) :
    board[i].append()


#상 하 좌 우 아래 위
dx = [-1,1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,1,-1]
result =0
que =deque()
def bfs() :
    global result, que
    while que :
        z,x,y = que.popleft()
        for i in range(6) :
            nz = z + dz[i]
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nz < 0 or nx>=N or ny >= M or nz>=H :
                continue
            if board[nz][nx][ny] == 0 :
                board[nz][nx][ny] = board[z][x][y] + 1
                que.append((nz,nx,ny))
                result = board[nz][nx][ny]
            if board[nz][nx][ny] == -1 :
                continue
    for i in range(H) :
        for j in range(N) :
            for k in range(M) :
                if board[i][j][k] == 0 :
                    return -1
    if result == 0 :
        return result
    else :
        return result -1

for i in range(H) :
        for j in range(N) :
            for k in range(M) :
                if board[i][j][k] == 1 :
                    que.append((i,j,k))

print(bfs())
