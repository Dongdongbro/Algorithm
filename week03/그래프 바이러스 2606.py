import sys
input = sys.stdin.readline

def find_parent(parent, x) :
    if parent[x] != x :
        parent[x]= find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b) :
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a<b :
        parent[b] = a
    else :
        parent[a] = b

n = int(input())
e = int(input())

graph = [[] for i in range(n+1)]
parent = [0] * (n+1)

for i in range(1, n+1) :
    parent[i] = i

for i in range(e) :
    a, b= map(int,input().split())
    union_parent(parent, a, b)

for i in range(1, n+1) :
    find_parent(parent, i)

result =0
for i in range(2, n+1) :
    if parent[i] == 1 :
        result += 1
print(result)