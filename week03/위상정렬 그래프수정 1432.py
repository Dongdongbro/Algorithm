import sys, heapq
input = sys.stdin.readline
N = int(input())
graph = [[] for i in range(N+1)]
indegree = [0] * (N+1)
result = [0] * (N+1)
for i in range(1, N+1) :
    temp = [0] +list(map(int,input().rstrip()))
    for j in range(1,N+1) :
        if temp[j] == 1 : #1이 입력값으로 받으면
            graph[j].append(i) #받은 자리의 수에 해당 값을 넣어준다, 진입차수를 반대로 설정
            indegree[i] += 1
print(temp)
def topology_sort() :
    que = []
    for i in range(1, N+1) :
        if indegree[i] == 0 : #0인 부분부터 시작
            heapq.heappush(que, -i)
    n = N
    while que :
        now = -heapq.heappop(que)
        result[now] = n
        for i in graph[now] :
            indegree[i] -= 1
            if indegree[i] == 0 :
                heapq.heappush(que, -i)
        n -= 1

topology_sort()
if result.count(0) > 1:
    print(-1)
else :
    print(*result[1:])