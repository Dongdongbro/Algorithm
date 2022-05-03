import sys, heapq
input = sys.stdin.readline

n = int(input())
board = []
for i in range(n) :
    board.append(list(map(int,input().rstrip())))
visited = [[0] * n for _ in range(n)]

def dijkstra() :
    heap = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0] = 1
    heapq.heappush(heap, [0,0,0])
    while heap :
        a, x, y = heapq.heappop(heap)
        if x == n-1 and y == n-1 :
            print(a)
            return
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0<= ny < n and visited[nx][ny] == 0 :
                visited[nx][ny] = 1
                if board[nx][ny] == 0 :
                    heapq.heappush(heap,[a+1,nx,ny])
                else :
                    heapq.heappush(heap,[a,nx,ny])

dijkstra()
