import sys
input = sys.stdin.readline

a = int(input())
a_list = list(map(int,input().split()))
a_list.sort()
b = int(input())
b_list = list(map(int,input().split()))

def binary_search(data, target) :
    start = 0
    end = len(a_list)

    while start < end :
        mid = (start+end)//2
        if data[mid] == target :
            return True
        elif data[mid] < target :
            start = mid +1
        else:
            end = mid -1
    return False

for i in b_list :
    if binary_search(a_list, i) :
        print(1)
    else :
        print(0)


