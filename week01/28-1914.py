import sys


def move(a, x, y) :
    global data
    if a > 1 :
        move(a-1, x, 6-x-y)
    
    print(x,y)
   

    if a > 1 :
        move(a-1, 6-x-y, y)

n= int(sys.stdin.readline())
print(2**n-1)
if n <= 20 :
    move(n,1,3)
