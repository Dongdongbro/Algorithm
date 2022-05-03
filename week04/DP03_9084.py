import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    array = list(map(int,input().split()))
    M = int(input())
    dp = [0] * (M+1)
    dp[0] = 1
    print(array)
    for i in array :
        for j in range(1,M+1) :
            if j >= i :
                dp[j] += dp[j-i]
    print(dp[M])