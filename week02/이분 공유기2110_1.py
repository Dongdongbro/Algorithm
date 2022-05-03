import sys
input = sys.stdin.readline

a, b = map(int, input().split())
home = []
for i in range(a) :
    c = int(input())
    home.append(c)
home.sort()
start = 1
end = home[-1]-home[0]
result =0
while start <= end :
    count = 1
    mid = (start+end)//2
    standard = home[0]
    for j in range(1,len(home)) :
        if home[j] >= standard+mid :
            count += 1
            standard = home[j]

    if count >= b :
        start = mid +1
        result =mid
    else :
        end = mid -1

print(result)



