import sys
from collections import deque
input = sys.stdin.readline

a,b = map(int,input().split())
board = [[int(x) for x in input().rstrip()] for _ in range(a)]

# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x,y) :
    que = deque()
    que.append((x,y))
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx<0 or ny<0 or nx>=a or ny>=b :
                continue
            if board[nx][ny] == 0 :
                continue
            if board[nx][ny] ==1 :
                board[nx][ny] = board[x][y] +1
                que.append((nx,ny))
    return board[a-1][b-1]

print(bfs(0,0))


