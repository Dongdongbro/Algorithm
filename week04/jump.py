import sys
import heapq
input = sys.stdin.readline

N, M = map(int, input().split())
small = [int(input()) for _ in range(M)]
visit = [0] * (N+((2*N)**0.5)+1)
# print(visit)
# dp = [[0] * (N+1) for _ in range(N+1)]
# minMove = sys.maxsize

def bfs():
    heap = []
    heapq.heappush(heap, [1, 2, 1]) #count, i돌, x칸
    visit[2] = 1
    while heap:
        count, now, jump = heapq.heappop(heap)
        if now == N: # 현재 탐색하는 돌이 N이랑 같으면 결과 출력
            print(count)
            return
        if now in small: # 건너지 못하는 돌을 만났을 때는 컨티뉴
            continue

        if now < N: #N보다 돌이 작을 경우에 실행한다
            for x in [jump+1, jump, jump-1]:
                if x > 0:
                    next = now + x # 다음 돌은 현재 돌의 위치에서 건너뛰는 돌을 의미한다.
                    if visit[next] != x: #만약 돌의 방문위치 값에 x라는 값이 존재하지 않으면,
                        visit[next] = x
                        heapq.heappush(heap, [count+1, next, x])
                print(visit)

    print(-1)


bfs()
# import sys
# import heapq
# input = sys.stdin.readline

# N, M = map(int, input().split())
# small = [int(input()) for _ in range(M)]
# small.sort()

# def bfs():
#     heap = []
#     heapq.heappush(heap, [1, 2, 1]) #move, i돌, x칸
#     while heap:
#         move, i, x = heapq.heappop(heap)
#         if i == N:
#             print(move)
#             return
#         if i in small:
#             continue
#         if i < N:
#             heapq.heappush(heap, [move + 1, i + x+1, x+1])
#             heapq.heappush(heap, [move + 1, i + x, x])
#             if x >= 2:
#                 heapq.heappush(heap, [move + 1, i + x-1, x-1])
#     print(-1)
# bfs()