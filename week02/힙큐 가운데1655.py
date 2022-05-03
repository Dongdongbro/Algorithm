import sys
import heapq
input = sys.stdin.readline

#아이디어
# 1. leftheap에 최대 힙값을 넣고, rightheap에 최소 힙값을 넣어서 중간값을 찾는다
# 2. 만약 leftheap과 rightheap의 길이가 같으면 leftheap에 값을 넣어준다.
# 3. 만약 길이가 같지 않다면 rightheap에 값을 넣어준다.
# 4. 만약 leftheap의 최대값이 rightheap의 최소값보다 크면 안되니까 두개를 변수에 팝시켜서 해당 값들을 반대로 push해주도록 한다.
# 5. 두 힙의 길이가 같으면 어쨋든 가장 중간에 있는 두수중에서 작은 값을 말해야 하므로 left값을 result변수에 넣어주는게 맞고,
# 6. 만약에 길이가 다른 경우에는 무조건 leftheap쪽에 있는 최대 힙값이 중간값이 된다.

a = int(input())
leftheap = []
rightheap = []

for i in range(a) :
    nums = int(input())
    if len(leftheap) == len(rightheap) :
        heapq.heappush(leftheap, -nums)
    else :
        heapq.heappush(rightheap, nums)
    if rightheap and -leftheap[0] > rightheap[0] :
        bigger = heapq.heappop(leftheap)
        smaller = heapq.heappop(rightheap)
        heapq.heappush(leftheap, -smaller)
        heapq.heappush(rightheap, -bigger)
    print(-leftheap[0])


