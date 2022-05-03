import sys
from collections import deque

v, e = map(int,input().split())
indegree = [0] *(v+1)  #진입차수가 몇개인지 노드 별로 세주기 위한 변수
graph = [[] for i in range(v+1)] #노드 별로 인접 노드를 입력받기 위한 그래프

for i in range(e) :
    a, b = map(int, input().split())
    graph[a].append(b) # 노드에 인접한 노드값을 그래프에 넣는다
    indegree[b] += 1 # b로 들어가는 노드가 있으면 그 수만큼 세준다

def topology_sort() :
    result = []
    q= deque()
    for i in range(1, v+1) :
        if indegree[i] == 0 : # 진입차수가 0 인것을 찾아서 큐에 넣어준다
            q.append(i)

    while q :
        now = q.popleft() # 큐에 들어간값을 빼서 변수에 넣어준다
        result.append(now) # 뺀거를 출력해주어야기에 result 리스트에 넣어준다
        for i in graph[now] :
            indegree[i] -= 1 # 해줬으면 인접차수 하나를 줄여주기 위해 -1을 해준다
            if indegree[i] ==0 : # 만약 줄여줘서 진입차수가 0이면 큐에 다시 넣어준다
                q.append(i)

    for i in result :
        print(i, end =' ') # 결괏값 출력
topology_sort()