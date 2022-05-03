import sys
input = sys.stdin.readline
T = int(input())
for i in range(T):
    N = int(input())
    dp = [[0] for i in range(N+4)]
    dp[0] = 1
    dp[1] = 1
    dp[2] = 1
    dp[3] = 2

    for i in range(4,N) :
        dp[i] = dp[i-2] + dp[i-3]

    print(dp[N-1])
