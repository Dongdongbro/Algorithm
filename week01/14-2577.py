import sys
a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

result = list(str(a*b*c))

for num in range(0,10) :
    print(result.count(str(num)))



