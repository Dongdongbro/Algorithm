'''
행렬의 제곱을 처리하는 함수와, 행렬의 거듭제곱수를 짝수일때와 홀수일때를 나눠주는 함수를 만들어서 처리해준 결괏값을 처리해준다.
거듭제곱수 함수에서 짝수일때와 홀수일때 경우를 곱셈에서 푼 방식대로 푼다.
'''
import sys
input = sys.stdin.readline
a, b = map(int,input().split())
l = [list(map(int,input().split())) for i in range(a)]

# 먼저 b의 값이 홀수인지 짝수인지 판단하는 함수를 만들자
def holzzak(l,b) :
    if b == 1 :
        for i in range(len(l)):
            for j in range(len(l)) :
                l[i][j]%1000
        return l

    temp = holzzak(l,b//2)
    if b%2 == 0 :
        return multi(temp, temp)
    else :
        return multi(multi(temp, temp), l)


def multi(l1, l2) :
    result = [(len(l1)*[0]) for i in range(len(l1))]
    for i in range(len(l1)) :
        for j in range(len(l1)) :
            for k in range(len(l1)) :
                result[i][k] += l1[i][j]*l2[j][k]%1000
    return result

result = holzzak(l,b)

for i in result :
    for j in i :
        print(j%1000, end = ' ')
    print()