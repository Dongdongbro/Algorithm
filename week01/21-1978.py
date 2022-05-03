import sys
from typing import Counter
case = int(sys.stdin.readline())
nums = list(map(int,sys.stdin.readline().split()))

#소수의 개념을 생각해 보았을 때, 2부터 자기 자신의 제곱근까지의 수를 나눴을 때, 나머지가 0이나오면 소수가 아니다. 
count = 0
for num in nums : #리스트 수대로 반복문을 돌려준다.
    nono = 0
    if num>1 : #입력받은 수가 1보다 클경우, 2부터 수사이에 있는 값으로 나누어 판단한다.
        for i in range(2,num) :
            if num%i == 0 :
                nono += 1 #나머지가 하나라도 0으로 떨어진다면, 소수가 아니므로 아닌 수를 카운트 해준다. 
        if nono == 0 : #만약 소수가 아닌게 증명이 되었다면, 카운트 1을 올려준다.
            count += 1
print(count)
        
