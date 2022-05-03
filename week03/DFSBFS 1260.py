import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, v, visited) :
    visited[v] = True
    print(v, end= ' ')
    for i in graph[v] :
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, v, visited) :
    que = deque([v])
    visited[v] = True
    while que :
        v = que.popleft()
        print(v, end=' ')
        for i in graph[v] :
            if not visited[i] :
                que.append(i)
                visited[i] = True

N, M, V = map(int, input().split())
graph = [[] for i in range(N+1)]
for i in range(M) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1) :
    graph[i].sort()

visited = [False] * (N+1)

dfs(graph, V, visited)
print()
visited = [False] * (N+1)
bfs(graph, V, visited)