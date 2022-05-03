
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(v) :
    cnt = 0
    for i in graph[v] :
        if A[i] == 1 :
            cnt += 1 
        else :
            if i not in visited :
                visited.add(i)
                cnt += dfs(i)
            #여기서 3개
    return cnt


N = int(input())
A = [0] + list(map(int,input().rstrip()))
graph = [[] for i in range(N+1)]
for i in range(1,N) :
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = set()
result =0

for i in range(1, N+1) :
    if A[i] == 1 :
        for j in graph[i] :
            if A[j] == 1 : #여기서 일단 2개
                result += 1
    else :
        if i not in visited :
            visited.add(i)
            tmp = dfs(i)
            result += tmp * (tmp-1)


print(result)
