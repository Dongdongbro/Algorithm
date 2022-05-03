import sys

a = int(sys.stdin.readline())
a_list = list(map(int, sys.stdin.readline().split()))
a_list.sort()

start = 0
end = a-1
num = a_list[start] + a_list[end]
answer_start = start
answer_end = end

while start < end :
    total = a_list[start] + a_list[end]
    if abs(total) < abs(num) :
        num = abs(total)
        answer_start, answer_end = start, end
        if num == 0 :
            break

    if total < 0 :
        start += 1
    else :
        end -= 1

print(a_list[answer_start],a_list[answer_end])
