import sys
a = int(sys.stdin.readline())

if 1<=a<=9 :
    for i in range(1,10):
        print(a, '*', i,'=', a*i)
