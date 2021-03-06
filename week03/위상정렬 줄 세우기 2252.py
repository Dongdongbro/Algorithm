import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
indegree = [0] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M) :
    a, b = map(int,input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() :
    result = []
    que = deque()
    for i in range(1, N+1) :
        if indegree[i] ==0 :
            que.append(i)

    while que :
        now = que.popleft()
        result.append(now)
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                que.append(i)
    for i in result :
        print(i, end= ' ')
topology_sort()
