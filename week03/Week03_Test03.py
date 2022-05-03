from sys import stdin
from collections import deque

INF = int(1e9)
input = stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append([B, C])
start_factory, end_factory = map(int, input().split())

def bfs(mid):
    queue = deque()
    queue.append(start_factory)
    visited = [False] * (N + 1)
    while queue:
        x = queue.popleft()
        if x == end_factory:
            return True
        for node, cost in graph[x]:
            if mid - cost >= 0 and not visited[node]:
                visited[node] = True
                mid -= cost
                queue.append(node)
    return False

start, end = 0, INF
while start <= end:
    mid = (start + end) // 2
    if bfs(mid):
        end = mid - 1
    else:
        start = mid + 1
print(end)