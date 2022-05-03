import sys
input = sys.stdin.readline

a, b = map(int,input().split())
videos = list(map(int,input().split()))

start = sum(videos)//b
end = sum(videos)
result = end

while start<=end :

    mid = (start+end)//2
    if mid < max(videos) :
        start = mid + 1
        continue
    plus,count = 0,0
    for i in range(len(videos)) :
        if videos[i] > mid :
            break
        elif plus + videos[i] <= mid :
            plus += videos[i]
        else :
            plus = videos[i]
            count += 1
    if count <= b-1 :
        end = mid -1
        result = min(result, mid)
    else :
        start = mid + 1

print(result)