import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

n = int(input())
graph = [[] for i in range(n+1)]

def dfs(x,way) :
    for i in graph[x] :
        a, b= i
        if distance[a] == -1:
            distance[a] = way +b
            dfs(a, way + b)


for i in range(n-1) :
    a, b, c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])
# 1번 노드에서 가장 먼곳을 찾는다.
distance = [-1] * (n+1) 
distance[1] =0
dfs(1,0)
#나온 값에서 가장 먼 노드를 찾는다
start = distance.index(max(distance))
distance = [-1] * (n+1)
distance[start] =0
dfs(start, 0)

print(max(distance))