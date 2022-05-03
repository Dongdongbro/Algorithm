import sys
x,y = map(int,sys.stdin.readline().split())

data = list(map(int,sys.stdin.readline().split()))
for i in range(x) :
    if y>data[i] :
        print(data[i])



