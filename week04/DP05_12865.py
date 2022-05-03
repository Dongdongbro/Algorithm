import sys
input = sys.stdin.readline

N,K = map(int, input().split())
stuff = [[0,0]]
array = [[0 for i in range(K+1)] for j in range(N+1)]

for i in range(N) :
    stuff.append(list(map(int, input().split())))

for i in range(1,N+1) : # 물건의 정보를 받아온다
    for j in range(1, K+1) : #최대 무게값까지 차례대로 값을 받는다
        weight = stuff[i][0]
        value = stuff[i][1]

        if j < weight :
            array[i][j] = array[i-1][j]
        else :
            array[i][j] = max(value+array[i-1][j-weight], array[i-1][j])
print(array[N][K])