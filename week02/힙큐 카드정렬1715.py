'''
카드 정렬 문제!
아이디어 : 작은 숫자부터 더해나가는 방법이 제일 효율적인 방법일 것이라 생각한다!
코딩 :
- 리스트를 입력 받고, 그 안에서 뭔가를 해야할 것 같은데...우선 받는대로 heappush를 해주고...
- 조건은 뭐가 있을까? sum이란 함수를 만들어서 각각으 수를 더해주는 것만으로는 부족! 그럼 그 sum변수에서 새로운값을 더해주는 걸 만들어 주면 되겠다
'''

import sys, heapq
input = sys.stdin.readline

a = int(input())
hq = []
result =0

for i in range(a) :
    num = int(input())
    heapq.heappush(hq, num)

while len(hq) >1 :
    num1 = heapq.heappop(hq)
    num2 = heapq.heappop(hq)
    sum = num1+num2
    heapq.heappush(hq, sum)
    result += sum

print(result)