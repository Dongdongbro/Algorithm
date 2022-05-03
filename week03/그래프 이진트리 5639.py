# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(10**9)

# def postorder(nums) :
#     length = len(nums)

#     if length <= 1 :
#         return nums
#     for i in range(1, length) :
#         if nums[i] > nums[0] :
#             return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
#     return postorder(nums[1:]) + [nums[0]]

# preorder = []

# while True :
#     try :
#         preorder.append(int(input()))
#     except :
#         break
# preorder = postorder(preorder)

# for j in preorder :
#     print(j)

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
preorder =[]
while True :
    try :
        preorder.append(int(input()))
    except :
        break

def postorder(nums) :
    length = len(nums)
    if length <= 1 :
        return nums
    for i in range(1, length) :
        if nums[i] > nums[0] :
            return postorder(nums[1:i]) + postorder(nums[i:]) + [nums[0]]
    return postorder(nums[1:]) + [nums[0]]

preorder = postorder(preorder)
for i in preorder :
    print(i)