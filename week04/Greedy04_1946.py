import sys
input = sys.stdin.readline

T= int(input())
for _ in range(T):
    N = int(input())
    app = []
    for i in range(N):
        app.append(list(map(int,input().split())))
    app.sort()
    start = app[0][1]
    count =1
    for i in range(1,N) :
        if app[i][1] < start :
            count += 1
            start = app[i][1]
    print(count)