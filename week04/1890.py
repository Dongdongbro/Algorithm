import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]
dp = [[0 for i in range(N)] for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N) :
        row = i + array[i][j]
        col = j + array[i][j]
        if i == N-1 and j == N-1 :
            break

        if row < N :
            dp[row][j] += dp[i][j]
        if col < N :
            dp[i][col] += dp[i][j]

print(dp[N-1][N-1])