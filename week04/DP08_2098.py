import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int,input().split())) for i in range(N)]
INF = int(1e9)
dp = [[INF]*(1<<N) for i in range(N)]

def tsp(x,visited) :
    # 만약 visited가 1111이라면(다 방문했다면)
    if visited == (1<<N)-1 :
        if array[x][0] : #출발점으로 가는 경로의 값이 있다면
            return array[x][0]
        else : # 출발점으로 가는 경로가 0일때
            return INF

    # 만약 이미 최소비용이 계산되어 있다면
    if dp[x][visited] != INF :
        return dp[x][visited]

    # 여러가지 갈 수 있는 경로를 탐색하기 위한 for문 설정
    for i in range(1,N):
        if array[x][i] == 0 : # 해당 가는 경로의 값이 0이라면 갈 수가 없다
            continue
        #이미 방문한 도시라면 더이상 방문할 필요가 없다. 예를들이 vistied가 1001라는건 이전에 출발지인 1번째도시와 4번째도시를 방문했다는 뜻이고 i는 2,3,4번째 도시를 돌텐데 4번째 도시인 1000인 값이 visited와 비교했을 때,
        #1001과 1000의 4번째도시를 의미하는 첫번째 1의 값이 같기에 True가 된다. 그러면 해당 for문을 넘겨주도록 한다.
        if visited & (1<<i) :
            continue

        #점화식 부분
        dp[x][visited] = min(dp[x][visited], tsp(i, visited|(1<<i))+array[x][i])
    return dp[x][visited]
print(tsp(0,1))