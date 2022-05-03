import sys

a = int(sys.stdin.readline())
data = [0] *10001
for _ in range(a):
    num = int(sys.stdin.readline())
    data[num] = data[num] + 1

for i in range(10001) :
    if data[i] != 0 :
        for j in range(data[i]) :
            print(i)