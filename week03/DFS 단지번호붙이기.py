import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)
n= int(input())
graph = []
num = [] # 단지 아파트 갯수 담아두는 리스트

for i in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
def dfs(x,y) :
    global count
    if x<0 or y<0 or x>=n or y>=n :
        return False
    if graph[x][y] == 1:
        count += 1
        graph[x][y] =0
        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny)
        return True
    return False

result =0
for i in range(n):
    for j in range(n) :
        if dfs(i,j) == True:
            num.append(count)
            result += 1
            count =0

num.sort()
print(result)
for i in range(len(num)) :
    print(num[i])