import sys
input = sys.stdin.readline

N, K = map(int,input().split())
array = []
for i in range(N) :
    array.append(int(input()))
count = 0
for i in reversed(range(N)) :
    count += K//array[i]
    K = K%array[i]

print(count)