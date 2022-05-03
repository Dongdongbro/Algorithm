import sys
c = int(sys.stdin.readline())

for i in range(0, c) :
    nums = list(map(int,sys.stdin.readline().split()))
    avg = sum(nums[1:])/nums[0]
    count =0
    for score in nums[1:] :
        if score > avg:
            count += 1
    rate = count/nums[0]*100
    print(f"{rate:.3f}%")
