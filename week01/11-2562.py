import sys

data = []
for i in range(9) :
    data.append(int(sys.stdin.readline()))

"""
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
f = int(sys.stdin.readline())
g = int(sys.stdin.readline())
h = int(sys.stdin.readline())
i = int(sys.stdin.readline())
"""

print(max(data))
print(data.index(max(data))+1)