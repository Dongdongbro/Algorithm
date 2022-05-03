import sys

w,h = map(int,sys.stdin.readline().split())
n = int(sys.stdin.readline())
width = []
height = []

for i in range(n) :
    a,b = map(int,sys.stdin.readline().split())
    if a == 0 :
        height.append(b)
    elif a == 1 :
        width.append(b)
width.append(w)
height.append(h)

width.sort()
height.sort()

x = width[0]
y = height[0]

for j in range(len(width)-1) :
    x = max([x, width[j+1]-width[j]])
for k in range(len(height)-1) :
    y = max([y, height[k+1]-height[k]])

print(x*y)