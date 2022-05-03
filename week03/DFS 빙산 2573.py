import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
N, M = map(int, input().split())
board = []
for i in range(N) :
    board.append(list(map(int,input().split())))
# 얼마나 녹을 것인지 해당 인덱스에다가 저장해놓는다

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def melt(x, y) :
    cnt = 0 # 인접한 바다 갯수
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M:
            if board[nx][ny] == 0:
                cnt += 1

    if cnt != 0:
        return x, y, cnt
    else:
        return None

def dfs(x, y) :
    visited[x][y] = True
    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<N and 0<=ny<M:
            # visited가 True가 아닌데 board값이 0이 아니면
            if not visited[nx][ny] and board[nx][ny] != 0 :
                dfs(nx,ny)

answer = 0

while True:
    answer += 1

    # 1. 빙하 녹이기
    reduce = []  # x, y, 녹는 높이
    for x in range(1, N):
        for y in range(1, M):
            if board[x][y] != 0:
                h = melt(x, y)

                if h is not None:
                    reduce.append(h)

    for x, y, h in reduce:
        board[x][y] = board[x][y] - h if board[x][y] - h > 0 else 0
    cnt = 0
    visited = [[False] * M for _ in range(N)]

    for x in range(1, N):
        for y in range(1, M):
            if board[x][y] != 0 and not visited[x][y]:
                cnt += 1

                if cnt == 2:
                    break

                dfs(x, y)

    if cnt > 1:  # 종료 조건
        break

    if sum(map(sum, board[1:-1])) == 0:  # 빙하가 다 녹을때까지 덩어리가 1개?
        answer = 0
        break

# 출력
print(answer)