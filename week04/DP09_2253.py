import sys
input = sys.stdin.readline

N,M = map(int, input().split())
INF = int(1e9)
dp = [[INF]*(int((2*N)**0.5)+2) for i in range(N+1)]
stone = []
for i in range(M) :
    stone.append(int(input()))
dp[1][0] = 0

for i in range(2,N+1) : # 2번 돌부터 차례대로 검색하기 위한 반복문
    if i in stone : # 못건너가는 돌이 있다면 컨티뉴
        continue
    for j in range(1, int((2*i)**0.5)+1) :
        dp[i][j] = min(dp[i - j][j - 1], dp[i - j][j], dp[i - j][j + 1])+1

answer = min(dp[N])
if answer != INF :
    print(answer)
else :
    print('-1')

