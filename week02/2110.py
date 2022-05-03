import sys

a, b = map(int,sys.stdin.readline().split())
home = []
for i in range(a) :
    c = int(sys.stdin.readline())
    home.append(c)

home.sort()
start = 1
end = home[-1] - home[0]


result =0

while start <= end :
    count =1
    stand = home[0]
    mid = (start+end)//2
    for j in range(1, len(home)) :
        if home[j] >= stand + mid :
            count += 1
            stand = home[j]

    if count >= b :
        start = mid + 1
        result = mid
    else :
        end = mid -1

print(result)
