import sys

a= int(sys.stdin.readline())


def sum(n) :
    if n == 1:
        return 1
    elif n == 2 :
        return 2
    elif n == 3 :
        return 4
    elif n >3 :
        return sum(n-1)+sum(n-2)+sum(n-3)

for i in range(a) :
    b = int(sys.stdin.readline())

    print(sum(b))
