'''
아이디어 :
- 집과 사무실의 좌표가 각각 다를 수 있으니 우선 d 범위 안에 집과 사무실이 있는지 확인하기 위해 abs(집-사무실) <=d 여야하는 조건
- 그 값들을 어쨋든 정렬해줘야하까 집 사무실을 정렬을 해주고, 그 정렬해준 것을 다른 리스트에 넣어준다.
- 그 리스트의 값을 for문으로 돌려서 heapq을 써주면 되는데, 그 조건은 아래와 같다.
- 만약 힙에 아무것도 없으면 그냥 push해준다.
- 그렇지 않은 경우에, 만약 로드된 값에서 인덱스 [1]값에서 d만큼 빼준 값이 힙[0][0] 보다 클 경우에는 heappop()을 해주고 로드 값을 넣어준다.
- 그렇게 해서 len(heap)이 가장 긴 것을 찾아서 출력해주면 된다!!!!!
'''

import sys, heapq
input = sys.stdin.readline

a = int(input())
datas = []
for i in range(a) :
    b = list(map(int,input().split()))
    datas.append(b)
d = int(input())

rail = []
for data in datas :
    if abs(data[1]-data[0]) <= d :
        data = sorted(data)
        rail.append(data)
rail.sort(key = lambda x : x[1])

hp = []
answer =0
for data in rail :
    if len(hp) == 0 :
        heapq.heappush(hp, data)
    else :
        while hp[0][0] < data[1]-d :
            heapq.heappop(hp)
            if not hp :
                break
        heapq.heappush(hp, data)
    answer = max(answer, len(hp))

print(answer)


