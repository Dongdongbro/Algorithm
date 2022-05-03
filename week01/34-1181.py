import sys

a= int(sys.stdin.readline())
word = []
for _ in range(a) :
    word.append(sys.stdin.readline().strip())
re_set = list(set(word))
re_set.sort()
re_set.sort(key = len) #알파벳 갯수대로 정렬


for i in re_set :
    print(i)