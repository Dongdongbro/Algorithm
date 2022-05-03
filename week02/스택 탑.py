import sys
input = sys.stdin.readline

n = int(input())
tower = list(map(int,input().split()))
stack = []

for i in range(n) :
    height = tower[i]
    if len(stack) != 0 :
        while len(stack) != 0 :
            if stack[-1][0] < height :
                stack.pop()
                if len(stack) == 0 :
                    print(0, end=' ')

            elif stack[-1][0] > height :
                print(stack[-1][1]+1, end=' ')
                break

            else :
                print(stack[-1][1]+1, end=' ')
                stack.pop()
                break
        stack.append([height, i])
    else :
        print(0,end=' ')
        stack.append([height,i])




















# import sys
# r = sys.stdin.readline # 입력 받기
# n = int(r())
# t_list = list(map(int, r().split()))
# answer = []
# stk = []
# for i in range(n):
#     h = t_list[i]
#     if stk:
#         while stk:
#             if stk[-1][0] < h :
#                  stk.pop()
#                  if not stk:
#                      print(0, end=' ')
#             elif stk[-1][0] > h:
#                 print(stk[-1][1]+1, end=' ')
#                 break
#             else :
#                 print(stk[-1][1]+1, end=' ')
#                 stk.pop()
#                 break
#         stk.append([h, i])
#     else:
#         print(0, end=' ')
#         stk.append([h,i])

