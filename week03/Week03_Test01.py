import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int,input().split())
max = 100000
visited = [0] * (max+1)
que = deque()
que.append(a)
while que :
    x = que.popleft()
    if x == b :
        print(visited[x])
        break
    for nx in (x-1, x+1, x*2) :
        if 0<=nx<=max and not visited[nx] :
            visited[nx] = visited[x] +1
            que.append(nx)