# import sys
# input = sys.stdin.readline


# def sosu(n) :
#     if n <2 :
#         return False
#     for i in range(2, int(n**0.5)+1) :
#         if n % i == 0 :
#             return False
#     return True

# for _ in range(int(input())) :
#     a = int(input())

#     for i in range(a//2,-1,-1) :
#         if sosu(i) and sosu(a-i) :
#             print(i, a-i)
#             break

