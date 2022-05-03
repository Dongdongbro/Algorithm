import sys
import math
day, ngt, ttl = map(int, sys.stdin.readline().split())

n = (ttl-ngt)/(day-ngt)
print(n)
print(math.ceil(n))