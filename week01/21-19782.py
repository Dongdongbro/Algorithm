import sys

a = int(sys.stdin.readline())
b = list(map(int,sys.stdin.readline().split()))
count = 0

for j in b:
    nono = 0
    if j > 1:
        for k in range(2, int(j**0.5)+1):
            if j % k == 0:
                nono += 1
        if nono == 0:
            count += 1

print(count)
