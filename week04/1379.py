import sys
input = sys.stdin.readline

N = int(input())
array = [list(map(int,input().split())) for _ in range(N)]
array.sort(key=lambda x:x[1])
array.sort(key=lambda x:x[2])
print(array)

count = 1
finish = array[0][2]
for i in range(1,N) :
    if array[i][1] >= finish :
        count += 1
        finish = array[i][2]
print(count)