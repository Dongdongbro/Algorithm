input = __import__('sys').stdin.readline

N = int(input())
a = int(input())
graph = [list(map(int, input().split())) for i in range(a)]
board = [[] for i in range(N+1)]
visited = [0]*(N+1)
answer = []
cnt = 0

for i, j in graph :
    board[i].append(j)
    board[j].append(i)

def dfs(start) :
    global cnt
    visited[start] = 1
    for num in board[start] :
        if visited[num] == 0 :
            cnt += 1
            dfs(num)

dfs(1)
print(cnt)

'''
def solution(tickets):
    visited = [0]*len(tickets)
    answer = []


    def dfs(start, array, result, depth):
        if depth == len(visited):
            answer.append(result+[start])
            return
        for i in range(len(array)):
            s, e = array[i][0], array[i][1]
            if s == start and not visited[i]:
                visited[i] = 1
                dfs(e, array, result+[s], depth+1)
                visited[i] = 0

    dfs('ICN', tickets, [], 0)
    print(answer)
    return sorted(answer)[0]
'''