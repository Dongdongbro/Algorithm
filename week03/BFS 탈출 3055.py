import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int,input().split())
board = []
for i in range(R):
    board.append(list(map(str,input().strip())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

que = deque()

for i in range(R):
    for j in range(C) :
        if board[i][j] == '*' :
            que.append((i,j))
        elif board[i][j] == 'S' :
            board[i][j] = 0
            que.append((i,j))
# for i in range(R) :
#     print(board[i])
# print(que)
def bfs() :
    global que
    while que :
        x, y = que.popleft()
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny <0 or nx >= R or ny >= C :
                continue
            if board[x][y] == '*' :
                if board[nx][ny]== '.' :
                    board[nx][ny] = '*'
                    que.append((nx,ny))
                else :
                    continue
            if board[x][y] != 'D' or board[x][y] != '*' or board[x][y] != 'X' or board[x][y] != '.' :
                if board[nx][ny] == '.' :
                    board[nx][ny] = board[x][y] +1
                    que.append((nx,ny))
                if board[nx][ny] == 'D' :
                    return board[x][y]+1
                else :
                    continue

answer = bfs()
if answer == None :
    print("KAKTUS")
else :
    print(answer)
for i in range(R) :
    print(board[i])
