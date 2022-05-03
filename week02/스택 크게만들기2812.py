import sys
input = sys.stdin.readline

a, b = map(int, input().split())
c = list(input())
stack = []
d = b

for i in range(a) :
    while stack and d>0 and stack[-1] < c[i] :
        stack.pop()
        d -= 1
    stack.append(c[i])

print(''.join(stack[:a-b]))