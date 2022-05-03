import sys

a = int(sys.stdin.readline()) 

count = 0

for i in range(1,a+1):
    a_list = list(map(int, str(i))) # 1~a 까지 숫자의 list를 만든다
    if i < 100 :
        count += 1
    elif a_list[2]-a_list[1] == a_list[1]-a_list[0] :
        count += 1
print(count)
 


# a_list = list(map(int, str(a))) #받은 자리수를 하나의 변수로 받기 위한 설정 방법
# print(a_list)
# i = len(a_list)

# print(a_list[2]-a_list[1])

# if i <= 2 :
#    print(i)

# elif i ==3 :
#     if a_list[2]-a_list[1] == a_list[1]-a_list[0] :
#         for j in range(a-99) :
#             count += 1
#     print(count)

