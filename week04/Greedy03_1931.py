import sys
input = sys.stdin.readline

N = int(input())
array = []
for i in range(N):
    array.append(list(map(int,input().split())))
array.sort()
array.sort(key=lambda x:x[1])

count = 1
finish = array[0][1]
for i in range(1, N):
    if array[i][0] >= finish :
        count +=1
        finish = array[i][1]
print(count)