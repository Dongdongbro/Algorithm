import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap=[]

N_list = []
for i in range(N) :
    a = int(input())
    if a != 0 :
        heapq.heappush(heap, (-a,a))
    else :
        if len(heap) >= 1 :
            print(heapq.heappop(heap)[1])
        else :
            print(0)





