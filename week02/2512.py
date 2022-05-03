import sys
input = sys.stdin.readline

a = int(input())
a_list = list(map(int,input().split()))

limit = int(input())

start = 0
end = max(a_list)

while start <= end :
    total = 0
    mid = (start+end)//2
    for i in a_list :
        if i > mid :
            total += mid
        elif i <= mid :
            total += i
    if total <= limit :
        start = mid + 1
    else :
        end = mid - 1


print(end)