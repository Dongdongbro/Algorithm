import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())

def solve(A,B) :
    if B == 1 :
        return A%c

    temp = solve(A,B//2)
    if B%2 == 0 :
        return (temp**2)%c
    else :
        return (temp**2)*A%c

print(solve(a,b))