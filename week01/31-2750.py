import sys

a = int(sys.stdin.readline())
data = []
for i in range(a):
    inp = int(sys.stdin.readline())
    data.append(inp)

data.sort()

for j in range(len(data)) :
    print(data[j])