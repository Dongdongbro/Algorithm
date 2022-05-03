import sys
input = sys.stdin.readline

nums = input().rstrip().split('-')
array = []
for i in nums :
    plus = 0
    num = i.split('+')
    for j in num :
        plus += int(j)
    array.append(plus)
first = array[0]
for i in array[1:]:
    first -= i

print(first)