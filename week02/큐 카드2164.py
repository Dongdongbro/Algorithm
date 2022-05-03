import sys
from collections import deque
input = sys.stdin.readline

a = int(input())
que = deque([i for i in range(1,a+1)])

while len(que) > 1 :
    que.popleft()
    num = que.popleft()
    que.append(num)

print(que[0])
