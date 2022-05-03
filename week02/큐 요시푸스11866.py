import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int,input().split())
que = deque([i for i in range(1, N+1)])
result =[]

while que :
    for i in range(K-1) :
        num = que.popleft()
        que.append(num)
    remove = que.popleft()
    result.append(remove)

print("<"+", ".join(map(str,result))+">")



