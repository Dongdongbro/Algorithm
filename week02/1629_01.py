'''
아이디어...
예시 10의 11승을 12로 나눈 값을 찾아라...
10의 11승은 어떻게 구하냐??
거듭제곱을 하는 수가 짝수인지 홀수인지 나누자
짝수이면...10^4  -> (10^2)^2
홀수이면...10^5 -> (10^2)^2*10 이라는 매커니즘을 이용할 수 있다.
'''
import sys
input = sys.stdin.readline

a, b, c = map(int,input().split())
result = 0

