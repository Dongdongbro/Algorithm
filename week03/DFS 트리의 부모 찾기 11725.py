
import sys
input = sys.stdin.readline

a = int(input())
graph = [[] for i in range(a+1)]
visited = [False] * (a+1)
parent = [0] * (a+1)

for i in range(a-1) :
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

# 연결된 노드들로부터 부모가 없으면 부모로 설정해준다
def dfs(graph, start, visited) :
    visited[start] = True
    for i in graph[start] :
        if not visited[i] :
            parent[i] = start

            dfs(graph,i,visited)

dfs(graph, 1, visited)

for i in range(2,len(parent)) :
    print(parent[i], end=' ')