import sys

a, b = map(int,sys.stdin.readline().split())
level = []
for i in range(a) :
     c = int(sys.stdin.readline())
     level.append(c)

start = min(level)
end = max(level) + b
result =0
while start <= end :
    sum = 0
    mid = (start+end)//2
    for j in level :
        if j < mid :
            sum += mid-j
    if sum <= b :
        result = mid
        start = mid + 1
    else :
        end = mid - 1

print(result)

