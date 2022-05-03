import sys

n, m = list(map(int, sys.stdin.readline().split()))
n_list = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(n_list)
res = 0 #최종 mid값을 담을 변수.

while start <= end :
    total = 0 #자른 만큼의 합을 더하는 변수
    mid = (start+end)//2
    for i in n_list :
        if i > mid :
            total += i-mid

    if total < m :
        end = mid - 1
    else :
        start = mid+1
print(end)