#뱀, 큐를 이용한 문제
import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
board = [[0]*N for i in range(N)]

K = int(input())
for i in range(K) :  #사과 위치에 1 값을 넣기
    r, c = map(int,input().split())
    board[r][c] = 1

#방향전환 경로 받기
L = int(input())
change = []
for i in range(L) :
    far, to = input().split()
    change[int(far)] = to
position = deque([[0, 0]])   #뱀머리부터 꼬리까지 데이터를 저장해주는 역할을 해준다

#순서대로 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
d = 1  # 처음에는 동쪽이므로 dx, dy의 [1] 인덱스 가져오기 위해 1로 설정
t = 0 # 시간초 나중에 +해줄것
nx, ny = 0,0 #늘려가며 position안에 있는지 판별하고 경계와 부딪히는지 판별

def boundary(x,y) :
    if x >=0 and x<N and y >=0 and y <N :
        return True
    else :
        return False

def turning(direction):
    global d
    if direction == 'D' :
        d = (d+1)%4 #원래 오른쪽으로 가면 인덱스를 하나씩 추가해주면 되지만 4로 나눈 나머지는 d값이 계속 커지거나 작아질 수 있기 때문이다.
    else :
        d = (d-1)%4
    return d

while True :
    t += 1
    nx += dx[d]
    ny += dy[d]

    if t in change.keys() :  # 입력받은 방향전환 정보의 초와 뱀이 움직이고 있는 t가 같아지면 방향전환 함수를 실행
        d = turning(change[t])

    if boundary(nx, ny) :
        if [nx,ny] in position :
            break
        # 사과가 있는 곳에 가면 0으로 다시 바꿔주고, 뱀의 머리 부분에 해당 좌표를 넣어준다.
        if board[nx][ny] ==1 :
            board[nx][ny] = 0
            position.append([nx,ny])
        # 사과가 없는 곳에 가면 뱀의 머리 부분에 nx ny 넣어주고 꼬리부분을 삭제해준다
        if board[nx][ny] == 0 :
            position.append([nx,ny])
            position.popleft()
    else :
        break

print(t)














# # 끝을 만났을 때는 die
# # apple -> 몸길이 +1,
# # (0,0)부터 시작

# def Solution():
#     time = 0
#     # 북동남서
#     snake_array = []
#     direction = {0:(0,1), 1:(1,0),2:(0,-1),3:(-1,0)}
#     dir = 0 # 동쪽

#     # empty:0, 사과:1, 뱀:2
#     nx,ny = 0,0
#     board[0][0] = 2 # start
#     snake_array.append([0,0])

#     # 끝날때까지 돌기
#     while(1):
#         time += 1
#         nx = nx + direction[dir][0]
#         ny = ny + direction[dir][1]

#         if not 0<= nx <N or not 0<= ny <N:
#              break

#     	# apple
#         if board[nx][ny] == 1:
#             board[nx][ny] = 2 # 머리 이동
#             snake_array.append([nx,ny])

#         # empty
#         elif board[nx][ny] == 0:
#             board[nx][ny] = 2
#             snake_array.append([nx,ny])
#             del_x, del_y = snake_array.pop(0)
#             board[del_x][del_y] = 0

#         # snake 몸통
#         elif board[nx][ny] == 2:
#             break

#         if len(snake_dir) != 0 and time == snake_dir[0][0]:
#                 time, new_dir = snake_dir.pop(0)
#                 if new_dir == 'L': # 왼쪽
#                     dir = (dir + 3) % 4
#                 elif new_dir == 'D':
#                     dir = (dir + 1) % 4

#     return time

# # 오른쪽/ 왼쪽 방향 바꾸는 건 % 연산자 이용하여 쉽게 할 수 있음
# # 왼쪽으로 돌리기 = (현재 방향 + 3) % 4
# # 오른쪽으로 돌리기 = (현재 방향 + 1) % 4
# # board
# N = int(input())
# board = [[0 for i in range(N)] for j in range(N)]

# # apple 넣기
# k = int(input())
# apple_locs = []
# for _ in range(k):
#     x, y = map(int, input().split())
#     board[x-1][y-1] = 1

# # snake 시간, 방향
# l = int(input())
# # (sec, c(left) or d(right))
# snake_dir = list(map(lambda x:[int(x[0]),str(x[1])],\
#                      [input().split() for _ in range(l)]))
# print(Solution())