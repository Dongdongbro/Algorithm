import sys
input = sys.stdin.readline

a = int(input())
sticks = []
for i in range(a) :
    b= int(input())
    sticks.append(b)
max_stick = sticks[-1]
count = 1
for i in reversed(range(a)) :
    if sticks[i] > max_stick :
        count += 1
        max_stick = sticks[i]

print(count)

