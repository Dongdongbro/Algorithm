import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int,input().split())
coins = []
for i in range(a) :
    c = int(input())
    coins.append(c)
coins_ = set(coins)
check = [0 for i in range(b+1)]
que = deque()
for i in coins_ :
    if i > b :
        continue
    que.append([i,1])
    check[i] =1 # 체크를 해주는 이유는 예를들어서 1과 5라는 코인이 주어졌을때 1이 5번 사용되어서 비효율적으로 5가 되는 것을 막기위한 장치이다.
qquit = True
while que :
    val, cnt = que.popleft()
    if val == b :
        print(cnt)
        qquit = False
        break
    for coin in coins_ :
        if val +coin > b :
            continue
        if check[val+coin] ==0 :
            check[val+coin] =1
            que.append([val+coin, cnt+1])

if qquit:
    print(-1)