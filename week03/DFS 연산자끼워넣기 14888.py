import sys
input = sys.stdin.readline

maximum = -1e9
minimum = 1e9

def dfs(long, total, plus, minus, multi, divide) :
    global maximum
    global minimum
    if long == n:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus > 0 :
        dfs(long+1, total+num[long] ,plus-1, minus, multi, divide)
    if minus > 0 :
        dfs(long+1, total-num[long], plus, minus-1,multi,divide)
    if multi > 0:
        dfs(long+1, total*num[long],plus, minus,multi-1,divide)
    if divide > 0:
        dfs(long+1, int(total/num[long]),plus, minus,multi,divide-1)

n = int(input())
num = list(map(int, input().split()))
method = list(map(int, input().split()))

dfs(1, num[0], method[0], method[1], method[2], method[3])

print(maximum)
print(minimum)