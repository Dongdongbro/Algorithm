import sys
from tracemalloc import start


n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
n_list.sort()
m = int(sys.stdin.readline())
m_list = list(map(int, sys.stdin.readline().split()))

def binary_search(data,target):
    start = 0
    end = len(data)

    while start < end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return None

for target in m_list:
    if binary_search(n_list,target):
        print(1)
    else:
        print(0)