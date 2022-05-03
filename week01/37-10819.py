def dfs(depth):
    if depth == N:
        result.append(sum(abs(li[i+1]-li[i]) for i in range(N-1)))
        return 
    for i in range(N):
        if check[i]:
            continue
        li.append(nums[i])
        check[i] = 1
        dfs(depth+1)
        li.pop()
        check[i] = 0

N = int(input())   # 리스트 갯수 받아주기
nums = list(map(int, input().split())) # 리스트에 들어갈 숫자를 넣어준다.
li, result = [], []  # li는 각 숫자들을 바꿔가며 넣어줄 하나의 리스트, result 더한 값들을 저장해주는 리스트
check = [0]*N   #
dfs(0)
print(max(result))