from collections import deque
input = __import__('sys').stdin.readline

n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m) :
    parent, child = map(int, input().split())
    graph[child].append(parent)
    graph[parent].append(child)
visited = [0] * (n+1)


def bfs(a) :
    que = deque()
    que.append(a)
    while que :
        h = que.popleft()
        for num in graph[h] :
            if visited[num] == 0 :
                que.append(num)
                visited[num] = visited[h] + 1

bfs(a)
if visited[b] == 0 : print(-1)
else : print(visited[b])


