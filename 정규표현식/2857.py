import re

result = []
num = 0

for _ in range(5):
    people = input()
    p = re.search('(FBI)',people)
    num += 1
    if p!= None :
        result.append(num)
if len(result)==0 :
    print('HE GOT AWAY!')
else :
    for i in result :
        print(i,end=' ')