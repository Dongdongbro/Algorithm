input = __import__('sys').stdin.readline
from collections import deque

a, b = map(int,input().split())
start_x, start_b, head = map(int,input().split())
que = deque()
board = []
for i in range(a) :
    board.append(list(map(int,input().split())))

# 북쪽이라면-> 서, 남, 동, 북 탐색
if head == 0 :
    dx = [0,1,0,-1]
    dy = [-1,0,1,0]
# 동 -> 북, 서, 남, 동
if head == 1 :
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
# 남 -> 동, 북, 서, 남
if head == 2 :
    dx = [0,-1,0,1]
    dy = [1,0,-1,0]
# 서 -> 남, 동, 북, 서
if head == 3 :
    dx = [1,0,-1,0]
    dy = [0,1,0,-1]
# 북쪽->서쪽, 서쪽->남쪽, 남쪽->동쪽, 동쪽->북쪽
# 북 0, 동 1, 남 2, 서 3

def bfs() :
    global que
    while que :
        x, y, head = que.popleft()
        # 북쪽이라면-> 서, 남, 동, 북 탐색
        if head == 0 :
            dx = [0,1,0,-1]
            dy = [-1,0,1,0]
        # 동 -> 북, 서, 남, 동
        if head == 1 :
            dx = [-1,0,1,0]
            dy = [0,-1,0,1]
        # 남 -> 동, 북, 서, 남
        if head == 2 :
            dx = [0,-1,0,1]
            dy = [1,0,-1,0]
        # 서 -> 남, 동, 북, 서
        if head == 3 :
            dx = [1,0,-1,0]
            dy = [0,1,0,-1]
        # 북쪽->서쪽, 서쪽->남쪽, 남쪽->동쪽, 동쪽->북쪽
        # 북 0, 동 1, 남 2, 서 3
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= a or ny >= b :
                continue
            if 


que.append((start_x, start_b, head))





'''
11 10
7 4 0
1 1 1 1 1 1 1 1 1 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 1 1 1 1 0 1
1 0 0 1 1 0 0 0 0 1
1 0 1 1 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 1 1 0 1
1 0 0 0 0 0 0 0 0 1
1 1 1 1 1 1 1 1 1 1
'''

#57