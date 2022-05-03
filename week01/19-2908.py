from cgi import print_exception
import sys

a,b = sys.stdin.readline().split()

c = int(a[::-1])
d = int(b[::-1])

if c>d :
    print(c)
else :
    print(d)