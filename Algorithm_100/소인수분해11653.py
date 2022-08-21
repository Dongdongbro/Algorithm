import sys
input = sys.stdin.readline

n = int(input())

def soinsu (n) :
    if n == 1 :
        return

    for i in range(2, n + 1) :
        if n % i != 0 :
            continue
        else :
            n = n // i
            print(i)
            soinsu(n)
            break

soinsu(n)