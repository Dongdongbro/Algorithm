import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N, M, K, X = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M) :
    a,b = map(int,input().split())
    graph[a].append(b)

visited = [False] * (N+1)
distance = [0] * (N+1)


def bfs(x) :
    answer =[]
    que =deque([x])
    visited[x] = True
    distance[x] =0
    while que :
        num = que.popleft()
        for i in graph[num] :
            if not visited[i] :
                visited[i] = True
                que.append(i)
                distance[i] = distance[num] + 1
                if distance[i] == K :
                    answer.append(i)

    if len(answer) == 0 :
        print(-1)
    else :
        answer.sort()
        for j in answer :
            print(j,end='\n')
bfs(X)





