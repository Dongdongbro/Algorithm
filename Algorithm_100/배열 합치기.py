input = __import__('sys').stdin.readline

a = input()
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ab = []

ab = A + B
ab.sort()
# [print(x, end = " ") for x in ab]
print(*ab)
