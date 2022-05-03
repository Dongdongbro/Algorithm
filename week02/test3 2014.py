import sys, heapq
input = sys.stdin.readline

a,b = map(int,input().split())
arr = list(map(int,input().split()))
heap = list(arr)
heapq.heapify(heap)

for i in range(b) :
    result = heapq.heappop(heap)
    for j in arr :
        heapq.heappush(heap, result*j)
        if result % j == 0 :    
            break

print(result)


# import heapq

# k, n = map(int, input().split())
# data = list(map(int, input().split()))
# heap = []

# for d in data:
#     heapq.heappush(heap, d)

# for _ in range(n):
#     num = heapq.heappop(heap)
#     for i in range(k):
#         temp = num * data[i]
#         heapq.heappush(heap, temp)

#         if num % data[i] == 0:
#             break

# print(num)