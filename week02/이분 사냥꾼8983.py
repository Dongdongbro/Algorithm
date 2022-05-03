# 동물을 기준으로 조건에 맞는 사냥꾼을 찾으면 count를 해주는 방식으로 진행
# 기준은 abs(사냥꾼-a)/b ==1 and b<=l 또는 이면 맞는조건을 생각...했지만 아니었다.

import sys
input = sys.stdin.readline

m, n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()
animal = [list(map(int,input().split())) for i in range(n)]

count = 0

for a,b in animal :
    start = 0
    end = len(position) -1
    while start < end :
        mid = (start+end)//2
        if position[mid] < a : # 동물의 x 축 기준으로 사냥꾼의 위치가 작은건 일단 넘겨준다
            start = mid + 1
        else : # x축 기준으로 사냥꾼의 위치가 같거나 크면 mid 값에 end을 설정해주고 찾는다
            end =mid
    if abs(position[end]-a)+b <= l or abs(position[end-1]-a)+b <= l : # 사냥꾼 end위치와 end-1 전에서 l범위 안에 있는지 판단한다.
        count +=1

print(count)