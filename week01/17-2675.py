import sys

a = int(sys.stdin.readline())

for j in range(a) :
    b = list(map(str, sys.stdin.readline().split()))
    
    c = list(b[1])
    d = int(b[0])
    for i in range(len(c)) :
        print(d*c[i],end="")
    print()