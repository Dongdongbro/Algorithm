import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
que =deque()
for i in range(M) :
    X, Y, K = map(int, input().split())
    graph[Y].append((X,K))
    indegree[X] += 1

board = [[0 for j in range(N+1)] for i in range(N+1)]

for i in range(1, N+1) :
    if not indegree[i] :
        que.append(i)
while que :
    now = que.popleft()
    for mid_idx, mid_val in graph[now] :

        if max(board[now]) == 0 :
            board[mid_idx][now] += mid_val
        # 중간 노드일 경우
        else :
            for i in range(1, N+1) :
                board[mid_idx][i] += mid_val * board[now][i]

        indegree[mid_idx] -= 1
        if indegree[mid_idx] == 0 :
            que.append(mid_idx)

for i in range(1,N+1) :
    if board[N][i] :
        print(i,board[N][i])