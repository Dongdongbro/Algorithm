input = __import__('sys').stdin.readline

a = input()

A = list(map(int,input().split()))
B = list(map(int,input().split()))

set1 = set(A)
set2 = set(B)

seta = set1-set2
setb = set2-set1
print(len(seta)+len(setb))