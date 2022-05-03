import sys

def fac(n) :
    if n == 0 : 
        return 1
    return n*fac(n-1) #n*n-1*n-2 .... 0까지 계산하기

a = int(sys.stdin.readline())
print(fac(a))
