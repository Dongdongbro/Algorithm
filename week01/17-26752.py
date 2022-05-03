import sys

a = int(sys.stdin.readline())

for i in range(a) :
    b = list(map(str, sys.stdin.readline().split()))
    c = int(b[0])
    d = list(b[1])
    for j in range(c) :
        print(c*d[j],end="")
    print()


