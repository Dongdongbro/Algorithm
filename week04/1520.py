import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
M,N = map(int,input().split())
array = [list(map(int,input().split())) for _ in range(M)]
dp = [[-1 for _ in range(N)] for k in range(M)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x,y) :
    count = 0
    if x == M-1 and y == N-1 :
        return 1
    if dp[x][y] != -1 :
        return dp[x][y]
    for i in range(4) :
        nx = x+dx[i]
        ny = y+dy[i]
        if 0 <= nx < M and 0 <= ny < N and array[x][y] > array[nx][ny] :
            count += dfs(nx,ny)
    dp[x][y] = count
    return dp[x][y]
print(dfs(0,0))