import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 100001


que = deque()
que.append(N)
while que :
    nuna = que.popleft()
    if nuna == K :
        print(visited[nuna])
        break
    for nx in (nuna-1,nuna+1,nuna*2) :
        if 0<=nx<=100000 and not visited[nx] :
            visited[nx] = visited[nuna] +1
            que.append(nx)