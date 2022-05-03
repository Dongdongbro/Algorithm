import sys

tall = [int(sys.stdin.readline()) for i in range(9)]

sum_ = sum(tall)
sub = sum_-100


for i in range(9) :
    for j in range(i+1,9) :
        if sub == tall[i] + tall[j]  :
            num1, num2 = tall[i], tall[j]
            tall.remove(num1)
            tall.remove(num2)
            tall.sort()

        
            for i in range(len(tall)) :
                print(tall[i])
            break

    if len(tall)<9:
        break






# import sys

# tall = []
# for i in range(9) :
#     a = int(sys.stdin.readline())
#     tall.append(a)

# sum_ = sum(tall)
# sub = sum_-100


# for i in range(9) :
#     for j in range(i+1,9) :
#         if sub == tall[i] + tall[j]  :
#             num1, num2 = tall[i], tall[j]
#             tall.remove(num1)
#             tall.remove(num2)
#             tall.sort()
            

