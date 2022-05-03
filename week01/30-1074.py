import sys
input = sys.stdin.readline
 
n, r, c = map(int, input().split())
 
# n: 변의 길이,x: 현재 위치의 x축 값, y:현재 위치의 y축 값
result = 0
def N(n, x, y):
    global result
 
    if x==r and y==c: # 0,0을 받았을 때는 result값에 저장되어 있는 값을 출력한다.
        print(int(result))
        exit(0)
 
    if n == 1: # 2x2 만 남았을 경우에 result에 1씩 추가해준다
        result += 1
        return
 
    if not(x<=r<x+n and y<=c<y+n): #1~4분면 차례대로 검증한다. 해당 분면에 존재하지 않으면 if 실행, 존재하면 그 안에서 또 아래 코드 실행
        result += n*n
        return
 
    # 1사분면
    N(n/2, x, y)
    # 2사분면
    N(n/2, x, y+n/2)
    # 3사분면
    N(n/2, x+n/2, y)
    # 4사분면
    N(n/2, x+n/2, y+n/2)
 
N(2**n, 0, 0)